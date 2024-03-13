import ipaddress
from lib.pycgminer import CgminerAPI
from concurrent.futures import ThreadPoolExecutor


def thread(ip):
    cgminer = CgminerAPI(ip)
    
    try:
        get_pools = cgminer.command('pools')
    except:
        return 'Error'
    else:
        if 'HotelFee' in str(get_pools):
            print(f'{ip} = (HotelFee)')

def main(ip_ranges):
    ip_list = []
    
    for range in ip_ranges:
        for ip in ipaddress.IPv4Network(range):
            ip_list.append(str(ip))
    
    pool = ThreadPoolExecutor(256)
    for ip in ip_list:
        pool.submit(thread, ip)
    
    pool.shutdown(wait=True)
    input('Close?... ')

if __name__ == '__main__':
    ip_ranges = []
    
    while True:
        ip_range = input('[IP-Range \ Start]: ')
        
        if ip_range.lower() == 'start':
            break
        else:
            ip_ranges.append(ip_range)
        
    main(ip_ranges)