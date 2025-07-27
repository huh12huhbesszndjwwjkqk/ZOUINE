# DeVloped By AbdeeLkarim Amiri

import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , xKEys , base64 , datetime , re ,socket , threading , http.client , ssl , gzip , asyncio , gc
from io import BytesIO
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import *
from datetime import datetime , timedelta
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from cfonts import render, say

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  
          
def MajorLoGin(PyL):
    context = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection("loginbp.common.ggbluefox.com", context=context)    
    headers = {
        'X-Unity-Version': '2018.4.11f1',
        'ReleaseVersion': 'OB49',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-GA': 'v1 1',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
        'Host': 'loginbp.common.ggbluefox.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'}
    try:
        conn.request("POST", "/MajorLogin", body=PyL, headers=headers)
        response = conn.getresponse()
        raw_data = response.read()
        if response.getheader('Content-Encoding') == 'gzip':
            with gzip.GzipFile(fileobj=BytesIO(raw_data)) as f:
                raw_data = f.read()                
        TexT = raw_data.decode(errors='ignore')
        if 'BR_PLATFORM_INVALID_OPENID' in TexT or 'BR_GOP_TOKEN_AUTH_FAILED' in TexT: sys.exit()
        return raw_data.hex() if response.status in [200,201] else None
    finally: conn.close() 

def OpEnUid(tK):
    R = requests.Session().get(f'https://100067.connect.garena.com/oauth/token/inspect?token={tK}').json()
    return R.get('open_id')
    
Thread(target = AuTo_ResTartinG , daemon = True).start()

def GeTToK():  
    with open("oussama.txt") as f: return f.read().strip()
          
class FF_CLient():

    def __init__(self):  
        self.empty_count = 0  
        self.reader = None ; self.writer = None          
        self.Get_FiNal_ToKen_0115()              
        
    async def sF(self):
        if self.writer:
            try: self.writer.close() ; await self.writer.wait_closed()
            except Exception as e: print(f' - Error CLose WriTer => {e}') ; restart_program()
        self.reader = None ; self.writer = None
        gc.collect()

    async def Connect_SerVer(self , Token , tok , host , port , key , iv):
        last_msg = None   
        while True:  
            try: 
                await self.sF()  
                self.reader, self.writer = await asyncio.wait_for(asyncio.open_connection(host , int(port)) , timeout = 4)  
                self.writer.write(bytes.fromhex(tok)) ; await self.writer.drain()    
                self.DaTa = await asyncio.wait_for(self.reader.read(1024) , timeout = 3)  
                if not self.DaTa or len(self.DaTa) == 0: raise Exception('No DaTa')
                self.writer.write(OpEnSq(key, iv)) ; await self.writer.drain()
                msg = '\n\x1b[1;98m [BoT SerVEr] => \x1b[1;92mAcTivE ! \x1b[1;97mConEcTed SuccEssFuLy !\x1b[1;97m\n'
                if msg != last_msg: print(msg) ; last_msg = msg  
                while True:  
                    try:  
                        self.DaTa = await asyncio.wait_for(self.reader.read(1024) , timeout = 10)  
                        if not self.DaTa:  
                            print(f' - aTTacH DaKhiL => [{self.empty_count}] !')  
                            self.empty_count += 1 ; await asyncio.sleep(0.5) ; break
                        self.writer.write(OpEnSq(key, iv)) ; await self.writer.drain()  
                    except (asyncio.TimeoutError , ConnectionResetError , ConnectionAbortedError , asyncio.IncompleteReadError , BrokenPipeError , OSError , Exception) as e: break 
                          
            except (asyncio.TimeoutError , ConnectionRefusedError , ConnectionResetError , ConnectionAbortedError , asyncio.IncompleteReadError , BrokenPipeError , OSError , Exception) as e: break
                
    def GeT_Key_Iv(self , serialized_data):
        my_message = xKEys.MyMessage()
        my_message.ParseFromString(serialized_data)
        timestamp , key , iv = my_message.field21 , my_message.field22 , my_message.field23
        timestamp_obj = Timestamp()
        timestamp_obj.FromNanoseconds(timestamp)
        timestamp_seconds = timestamp_obj.seconds
        timestamp_nanos = timestamp_obj.nanos
        combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos
        return combined_timestamp , key , iv  
                       
    def GeT_LoGin_PorTs(self , JwT_ToKen , PayLoad):
        self.UrL = 'https://clientbp.common.ggbluefox.com/GetLoginData'
        self.HeadErs = {
            'Expect': '100-continue',
            'Authorization': f'Bearer {JwT_ToKen}',
            'X-Unity-Version': '2018.4.11f1',
            'X-GA': 'v1 1',
            'ReleaseVersion': 'OB49',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)',
            'Host': 'clientbp.common.ggbluefox.com',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate, br',}       
        try:
                self.Res = requests.post(self.UrL , headers=self.HeadErs , data=PayLoad , verify=False)
                self.BesTo_data = json.loads(DeCode_PackEt(self.Res.content.hex()))  
                address2 = self.BesTo_data['14']['data'] 
                ip2 = address2[:len(address2) - 6]
                port2 = address2[len(address2) - 5:]        
                return ip2 , port2          
        except requests.RequestException as e:
                print(f" - Bad Requests !")
        print(" - Failed To GeT PorTs !")
        return None , None   
        
    def ToKen_GeneRaTe(self , A):
        try:
            if A == 'BesTo': 
                self.PLaFTrom = 3
                self.A = GeTToK()
                self.O = OpEnUid(self.A)
                print('AuTh => ' + self.A , self.O)
                self.Version , self.V = '2019118399' , '1.111.11'      
                self.PyL = {
                    3: str(datetime.now())[:-7] ,
                    4: "free fire",
                    5: 1,
                    7: self.V ,
                    8: "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)",
                    9: "Handheld",
                    10: "Verizon Wireless",
                    11: "WIFI",
                    12: 1280,
                    13: 960,
                    14: "240",
                    15: "x86-64 SSE3 SSE4.1 SSE4.2 AVX AVX2 | 2400 | 4",
                    16: 5951,
                    17: "Adreno (TM) 640",
                    18: "OpenGL ES 3.0",
                    19: "Google|0fc0e446-ca27-4faa-824a-d40d77767de9",
                    20: "20.171.73.202",
                    21: "vn",
                    22: self.O ,
                    23: self.PLaFTrom,
                    24: "Handheld",
                    25: "google G011A",
                    29: self.A ,
                    30: 1,
                    41: "Verizon Wireless",
                    42: "WIFI",
                    57: "1ac4b80ecf0478a44203bf8fac6120f5",
                    60: 32966,
                    61: 29779,
                    62: 2479,
                    63: 914,
                    64: 31176,
                    65: 32966,
                    66: 31176,
                    67: 32966,
                    70: 4,
                    73: 2,
                    74: "/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/lib/arm",
                    76: 1,
                    77: "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-g8eDE0T268FtFmnFZ2UpmA==/base.apk",
                    78: 6,
                    79: 1,
                    81: "32",
                    83: self.Version ,
                    86: "OpenGLES2",
                    87: 255,
                    88: self.PLaFTrom,
                    89: "J\u0003FD\u0004\r_UH\u0003\u000b\u0016_\u0003D^J>\u000fWT\u0000\\=\nQ_;\u0000\r;Z\u0005a",
                    90: "Phoenix",
                    91: "AZ",
                    92: 10214,
                    93: "3rd_party",
                    94: "KqsHT7gtKWkK0gY/HwmdwXIhSiz4fQldX3YjZeK86XBTthKAf1bW4Vsz6Di0S8vqr0Jc4HX3TMQ8KaUU3GeVvYzWF9I=",
                    95: 111207,
                    97: 1,
                    98: 1,
                    99: f"{self.PLaFTrom}" ,
                    100: f"{self.PLaFTrom}"}
            try:                  
                self.PyL = CrEaTe_ProTo(self.PyL).hex()        
                self.PaYload = bytes.fromhex(EnC_AEs(self.PyL))
            except: restart_program()
            self.ResPonse = MajorLoGin(self.PaYload)
            if self.ResPonse:
                self.BesTo_data = json.loads(DeCode_PackEt(self.ResPonse))
                self.JwT_ToKen = self.BesTo_data['8']['data']          
                self.combined_timestamp , self.key , self.iv = self.GeT_Key_Iv(bytes.fromhex(self.ResPonse))
                ip , port = self.GeT_LoGin_PorTs(self.JwT_ToKen , self.PaYload)
                return self.JwT_ToKen , self.key , self.iv, self.combined_timestamp , ip , port
        except Exception as e:
        	print(e)
        	restart_program()
        	      
    def Get_FiNal_ToKen_0115(self):
        A = 'BesTo'
        token , key , iv , Timestamp , ip , port = self.ToKen_GeneRaTe(A)
        self.JwT_ToKen = token        
        try:
            self.AfTer_DeC_JwT = jwt.decode(token, options={"verify_signature": False})
            self.AccounT_Uid = self.AfTer_DeC_JwT.get('account_id')
            self.Nm = self.AfTer_DeC_JwT.get('nickname')
            self.H , self.M , self.S = GeT_Time(self.AfTer_DeC_JwT.get('exp'))
            self.Vr = self.AfTer_DeC_JwT.get('release_version')
            self.EncoDed_AccounT = hex(self.AccounT_Uid)[2:]
            self.HeX_VaLue = DecodE_HeX(Timestamp)
            self.TimE_HEx = self.HeX_VaLue
            self.JwT_ToKen_ = token.encode().hex()
            os.system('clear')
            print(render('BooT', colors=['white', 'blue'], align='center'))
            print(f'\n\x1b[1;93m - STarTinG TurN TarGeT AccounT On !\x1b[1;97m\n\n - ProxCEd JwT => {token}\n\n - AccEss ToKen => {self.A}\n - OpEn Uid => {self.O}\n\n - ProxCEd Uid => {self.AccounT_Uid}\n - TarGeT Name => {self.Nm}\n - ReLEasE VErsioN => {self.Vr}\n - TarGeT JwT ExpirE => {self.H}H - {self.M}Min - {self.S}Sec\n - DeVLoper : AbdeeLkarim Amiri')
        except Exception as e:
            print(f" - Error In ToKen : {e}")
            return
        try:
            self.Header = hex(len(EnC_PacKeT(self.JwT_ToKen_, key, iv)) // 2)[2:]
            length = len(self.EncoDed_AccounT)
            self.__ = '00000000'
            if length == 9: self.__ = '0000000'
            elif length == 8: self.__ = '00000000'
            elif length == 10: self.__ = '000000'
            elif length == 7: self.__ = '000000000'
            else:
                print('Unexpected length encountered')                
            self.Header = f'0115{self.__}{self.EncoDed_AccounT}{self.TimE_HEx}00000{self.Header}'
            self.FiNal_ToKen_0115 = self.Header + EnC_PacKeT(self.JwT_ToKen_, key, iv)
        except Exception as e:
            print(f" - Erorr In Final Token : {e}")            
        self.AutH_ToKen = self.FiNal_ToKen_0115
        asyncio.run(self.Connect_SerVer(self.JwT_ToKen, self.AutH_ToKen, ip, port, key, iv))
        return self.AutH_ToKen , key , iv
  

def StarT_SerVer():
    FF_CLient()

StarT_SerVer()