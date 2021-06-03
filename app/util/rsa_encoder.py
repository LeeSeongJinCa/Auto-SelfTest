from base64 import b64encode
from Crypto.Cipher import PKCS1_v1_5
from Cryptodome.PublicKey.RSA import construct


class RSAEncoder:
    def __init__(self):
        self.e = 65537
        self.n = 30718937712611605689191751047964347711554702318809238360089112453166217803395521606458190795722565177328746277011809492198037993902927400109154434682159584719442248913593972742086295960255192532052628569970645316811605886842040898815578676961759671712587342568414746446165948582657737331468733813122567503321355924190641302039446055143553127897636698729043365414410208454947672037202818029336707554263659582522814775377559532575089915217472518288660143323212695978110773753720635850393399040827859210693969622113812618481428838504301698541638186158736040620420633114291426890790215359085924554848097772407366395041461
        self.public_key = construct((self.n, self.e))
        self.cipher = PKCS1_v1_5.new(self.public_key)

    def encode(self, string):
        return b64encode(self.cipher.encrypt(bytes(string, "utf-8"))).decode()