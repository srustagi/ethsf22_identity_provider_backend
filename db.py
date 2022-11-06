import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
from web3 import Web3
from eth_account.messages import encode_defunct

# Load environment variables
load_dotenv()

# Helper Functions
def env(var):
  return os.environ.get(var)

# Initialize Firebase
cred = credentials.Certificate(env('FIREBASE_JSON'))
app = firebase_admin.initialize_app(cred)
db = firestore.client()


def v_t(user):
  message = f'{user.get("address")} is proving their Twitter account {user.get("twitter").get("handle")}.'
  return verify_twitter_proof(user.get('address'), user.get("twitter").get("handle"), message, user.get("twitter").get("signature"))

def verify_twitter_proof(address, handle, message, signature):
  w3 = Web3(Web3.HTTPProvider(''))
  tmp_msg = encode_defunct(text=message)
  recovered_address = w3.eth.account.recover_message(tmp_msg, signature=signature)
  print(recovered_address)
  return recovered_address == address, handle

def get_user(address):
  doc_ref = db.collection(u'users').document(address)
  doc = doc_ref.get()
  if doc.exists:
    return {'address': address, **doc.to_dict()}
  else:
    return None
