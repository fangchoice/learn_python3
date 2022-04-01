
#
# 1. pip install bleak
# 2. pip install loguru
#


import asyncio
from configparser import ConfigParser
from bleak import BleakScanner, BleakClient, discover
from loguru import logger

DATA = []
SUCC = []
FAIL = []
BT = []
BT_SUCC = []


async def scan():
    """ 扫描蓝牙设备
    """
    dev = await discover()
    for i in range(0, len(dev)):

        print("[" + str(i) + "] " + dev[i].address,
              dev[i].name, dev[i].metadata["uuids"],  dev[i].rssi)


async def main():
    dev = await BleakScanner.discover()
    for d in dev:
        print(d)


def notification_handler(sender, data):
    """ 回调函数： 收到 pen ---> app 信息
    """
    print(', '.join('{:02x}'.format(x) for x in data))
    if bytes(data).startswith(b'\x00\x08\x03'):
        DATA.append(bytes(data))
        # print(bytes(data))
    if bytes(data).startswith(b'\xf5\x01\x00'):
        BT.append(bytes(data))


def len_conv(data):
    """ MCU 和 BT 长度转换方法
    """
    return int(data[0] & 0xff | (data[1] & 0xff) << 8 | (data[2] & 0xff) << 16 | (data[3] & 0xff) << 24)


def check_crc(crc_val):
    """ 校验 MCU 数据的 CRC
    """

    table = [
        0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50A5, 0x60C6, 0x70E7,
        0x8108, 0x9129, 0xA14A, 0xB16B, 0xC18C, 0xD1AD, 0xE1CE, 0xF1EF,
        0x1231, 0x0210, 0x3273, 0x2252, 0x52B5, 0x4294, 0x72F7, 0x62D6,
        0x9339, 0x8318, 0xB37B, 0xA35A, 0xD3BD, 0xC39C, 0xF3FF, 0xE3DE,
        0x2462, 0x3443, 0x0420, 0x1401, 0x64E6, 0x74C7, 0x44A4, 0x5485,
        0xA56A, 0xB54B, 0x8528, 0x9509, 0xE5EE, 0xF5CF, 0xC5AC, 0xD58D,
        0x3653, 0x2672, 0x1611, 0x0630, 0x76D7, 0x66F6, 0x5695, 0x46B4,
        0xB75B, 0xA77A, 0x9719, 0x8738, 0xF7DF, 0xE7FE, 0xD79D, 0xC7BC,
        0x48C4, 0x58E5, 0x6886, 0x78A7, 0x0840, 0x1861, 0x2802, 0x3823,
        0xC9CC, 0xD9ED, 0xE98E, 0xF9AF, 0x8948, 0x9969, 0xA90A, 0xB92B,
        0x5AF5, 0x4AD4, 0x7AB7, 0x6A96, 0x1A71, 0x0A50, 0x3A33, 0x2A12,
        0xDBFD, 0xCBDC, 0xFBBF, 0xEB9E, 0x9B79, 0x8B58, 0xBB3B, 0xAB1A,
        0x6CA6, 0x7C87, 0x4CE4, 0x5CC5, 0x2C22, 0x3C03, 0x0C60, 0x1C41,
        0xEDAE, 0xFD8F, 0xCDEC, 0xDDCD, 0xAD2A, 0xBD0B, 0x8D68, 0x9D49,
        0x7E97, 0x6EB6, 0x5ED5, 0x4EF4, 0x3E13, 0x2E32, 0x1E51, 0x0E70,
        0xFF9F, 0xEFBE, 0xDFDD, 0xCFFC, 0xBF1B, 0xAF3A, 0x9F59, 0x8F78,
        0x9188, 0x81A9, 0xB1CA, 0xA1EB, 0xD10C, 0xC12D, 0xF14E, 0xE16F,
        0x1080, 0x00A1, 0x30C2, 0x20E3, 0x5004, 0x4025, 0x7046, 0x6067,
        0x83B9, 0x9398, 0xA3FB, 0xB3DA, 0xC33D, 0xD31C, 0xE37F, 0xF35E,
        0x02B1, 0x1290, 0x22F3, 0x32D2, 0x4235, 0x5214, 0x6277, 0x7256,
        0xB5EA, 0xA5CB, 0x95A8, 0x8589, 0xF56E, 0xE54F, 0xD52C, 0xC50D,
        0x34E2, 0x24C3, 0x14A0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405,
        0xA7DB, 0xB7FA, 0x8799, 0x97B8, 0xE75F, 0xF77E, 0xC71D, 0xD73C,
        0x26D3, 0x36F2, 0x0691, 0x16B0, 0x6657, 0x7676, 0x4615, 0x5634,
        0xD94C, 0xC96D, 0xF90E, 0xE92F, 0x99C8, 0x89E9, 0xB98A, 0xA9AB,
        0x5844, 0x4865, 0x7806, 0x6827, 0x18C0, 0x08E1, 0x3882, 0x28A3,
        0xCB7D, 0xDB5C, 0xEB3F, 0xFB1E, 0x8BF9, 0x9BD8, 0xABBB, 0xBB9A,
        0x4A75, 0x5A54, 0x6A37, 0x7A16, 0x0AF1, 0x1AD0, 0x2AB3, 0x3A92,
        0xFD2E, 0xED0F, 0xDD6C, 0xCD4D, 0xBDAA, 0xAD8B, 0x9DE8, 0x8DC9,
        0x7C26, 0x6C07, 0x5C64, 0x4C45, 0x3CA2, 0x2C83, 0x1CE0, 0x0CC1,
        0xEF1F, 0xFF3E, 0xCF5D, 0xDF7C, 0xAF9B, 0xBFBA, 0x8FD9, 0x9FF8,
        0x6E17, 0x7E36, 0x4E55, 0x5E74, 0x2E93, 0x3EB2, 0x0ED1, 0x1EF0,
    ]

    crc = 0x0000
    for i in range(len(crc_val)):
        crc = ((crc << 8) ^ table[((crc >> 8) ^ (0xff & crc_val[i]))]) & 0xFFFF

    head_0 = (crc >> 8) & 0xff  # 109
    head_1 = (crc & 0xff)

    return [head_0, head_1]


def crc16(data, _len):
    """ 校验 BT 数据的 CRC
    """
    poly = [0, 0xA001]
    crc = 0xFFFF
    ds = 0
    for i in range(_len):
        ds = data[i]
        for _ in range(8):
            crc = (crc >> 1) ^ poly[(crc ^ ds) & 1] & 0xFFFF
            ds = ds >> 1

    return crc


def bt_conv_data(index, data):
    """ 拼接 BT 数据 (head + bt_data + crc)
    """
    head = bytes([index & 0xff, (index >> 8) & 0xff])
    _crc_val = crc16(head + data, len(head + data))
    crc = bytes([_crc_val & 0xFF, ((_crc_val >> 8) & 0xFF)])
    _bt_data = head + data + crc

    return _bt_data


def end_ota(index):
    """ 发送蓝牙的结束包命令
    """

    a = (index - 1) & 0xff
    b = ((index - 1) >> 8) & 0xff
    c = (~(index - 1)) & 0xff
    d = ((~(index - 1)) >> 8) & 0xff

    buf = bytes([0x02, 0xff, a, b, c, d])
    crc = crc16(buf, 6)
    crc_val = bytes([crc & 0xff, (crc >> 8) & 0xff])

    print(bytes.hex(buf+crc_val), len(buf+crc_val))

    return buf + crc_val


async def read_file(filename, client, uuid):
    """ 读取mcu+bt 的合并文件，并发送相应的数据
    """

    with open(filename, 'rb') as f:
        data = f.read()

        head = data[:3]
        file_type = data[3]
        pen_type = data[4]
        bt_ver = data[5:15]
        bt_len = data[15:19]
        mcu_ver = data[19:29]
        mcu_len = data[29:33]
        md5 = data[33:49]

        if head != b"TQL":
            logger.info(" File Formater Error")
            return

        valid_data = [head, file_type, pen_type,
                      bt_ver, bt_len, mcu_ver, mcu_len, md5]

        bt_len_int10 = int(bytes.hex(bt_len), 16)

        mcu_len_int10 = int(bytes.hex(mcu_len), 16)

        _mcu_len = len_conv(mcu_len)
        print('_len _mcu:', _mcu_len)

        _bt_len = len_conv(bt_len)
        print('_bt _len:', _bt_len)
        print('mcu + bt len:', _bt_len+_mcu_len)

        N1 = data[49:49+_mcu_len]
        N2 = data[49+_mcu_len:49+_mcu_len+_bt_len]

        # --------------------------------------------------------------------------------------------------------
        # MCU
        crc_byte = check_crc(N1)
        print(crc_byte)

        is_bt = 0x01 if mcu_len_int10 > 0 else 0x00
        # is_bt = 0x00
        cmd1 = [0x00, 0x08, 0x03, 0x00, 0x07, mcu_len_int10 & 0xFF, (
            mcu_len_int10 >> 8) & 0xFF, (mcu_len_int10 >> 16) & 0xFF, (mcu_len_int10 >> 24) & 0xFF, is_bt, crc_byte[1], crc_byte[0]]

        await client.write_gatt_char(uuid, bytes(cmd1))

        logger.info(
            f" Start To Send Update Command {' '.join(('{:02x}'.format(x)).upper() for x in bytes(cmd1))}")

        off_uuid = "0000f201-0000-1000-8000-00805f9b34fb"
        await asyncio.sleep(1.0)

        # 20 bytes a packet
        mcu_div = _mcu_len % 20
        mcu_pkt_cnt = (_mcu_len // 20) + 1 if mcu_div else _mcu_len // 20

        # pkt = _mcu_len // 20
        _div = mcu_pkt_cnt % 40  # 是否被 40 整除
        count = mcu_pkt_cnt // 40 + 1 if _div else mcu_pkt_cnt // 40

        for i in range(count):
            _data_8 = N1[i*800:(i+1)*800]
            _len_800 = len(_data_8)
            if DATA:
                val = DATA.pop()
                print('val:', val)

                if val.startswith(b'\x00\x08\x03'):
                    _cnt = _len_800 // 20 + 1 if _len_800 % 20 else _len_800 // 20
                    for j in range(_cnt):
                        _j_data = _data_8[j*20:(j+1)*20]

                        await client.write_gatt_char(off_uuid, _j_data)
                        await asyncio.sleep(0.03)
            await asyncio.sleep(0.1)

        await asyncio.sleep(1.0)
        if DATA:
            val = DATA.pop()
            print('val succ:', val)
            if val.startswith(b'\x00\x08\x03\x01\x01\x00'):
                await client.write_gatt_char(uuid, bytes([0x00, 0x08, 0x03, 0x03, 0x01, 0x00]))
                SUCC.append('success')

                logger.info(f" MCU Update Success {len(SUCC)} Times ")

            elif val.startswith(b'\x00\x08\x03\x01\x01\x01'):

                FAIL.append('fail')
                logger.info(f" MCU Update Failure {len(FAIL)} Times ")

            else:

                FAIL.append('timeout')
                logger.info(f" MCU Update Failure {len(FAIL)} Times ")

        # --------------------------------------------------------------------------------------------------------
        # BT
        await asyncio.sleep(1.0)
        await client.write_gatt_char(uuid, bytes([0xF4, 0x01, 0xFF]))
        logger.info(" Start To Update BT: F4 01 FF ")
        await asyncio.sleep(1.0)

        # 20 bytes a packet
        bt_uuid = "00010203-0405-0607-0809-0a0b0c0d2b12"
        bt_div = _bt_len % 16
        bt_pkt_cnt = (_bt_len // 16) + 1 if bt_div else _bt_len // 16
        print(_bt_len // 16, bt_pkt_cnt)

        if BT:
            val = BT.pop()
            print('val:', val)
            await client.write_gatt_char(bt_uuid, bytes([0x01, 0xFF]))
            for i in range(bt_pkt_cnt - 1):
                await asyncio.sleep(0.01)
                bt_data = N2[i*16:(i+1)*16]

                _bt_data = bt_conv_data(i, bt_data)
                await client.write_gatt_char(bt_uuid, _bt_data)

            # 最后一包
            await asyncio.sleep(0.01)
            last_pkt = N2[(bt_pkt_cnt-1)*16:]
            last_len = len(last_pkt)
            if last_len == 16:

                _bt_data = bt_conv_data(bt_pkt_cnt - 1, last_pkt)
                await client.write_gatt_char(bt_uuid, _bt_data)

            else:
                sup = b'\xFF'
                add = 16 - last_len
                new_data = last_pkt + sup*add

                _bt_data = bt_conv_data(bt_pkt_cnt - 1, new_data)
                await client.write_gatt_char(bt_uuid, _bt_data)

                print(bytes.hex(_bt_data), len(_bt_data))

            # BT update success
            BT_SUCC.append('bt_succ')
            logger.info(f" BT Update Success {len(BT_SUCC)} Times ")
            # 结束命令
            await asyncio.sleep(0.01)
            end_val = end_ota(bt_pkt_cnt)
            await client.write_gatt_char(bt_uuid, end_val)


async def write_data(addr, filename, count):
    wuuid = "0000f102-0000-1000-8000-00805f9b34fb"
    ruuid = "0000f101-0000-1000-8000-00805f9b34fb"
    ota = "00010203-0405-0607-0809-0a0b0c0d2b12"

    off_ruuid = "0000f202-0000-1000-8000-00805f9b34fb"

    for _ in range(count):
        async with BleakClient(addr) as client:

            await client.start_notify(ruuid, notification_handler)

            # send cmd
            await read_file(filename, client, wuuid)

            await asyncio.sleep(20)

if __name__ == '__main__':
    # read config
    conf = ConfigParser()
    conf.read('conf.ini', encoding='utf-8')
    filename = conf['info']['path']
    addr = conf['info']['mac']
    count = int(conf['info']['nums'])

    # log
    logger.add("mcu_bt_{time}.log", rotation="500 MB",
               format="{time} {level} {message}", level="INFO")

    # update mcu and bt
    asyncio.run(write_data(addr, filename, count))
    print(f'Success Nums : {len(SUCC)}')
