# decentralized identity system

## create identity
1. sign with ethereum 
    - *v1*: walletconnect, no message signed
    - *v2*: proper sign message
2. store json object in file
    - `{address: {twitter: <proof_string>, github: <proof_string>, ssh?: <proof_string>, linkedn: <proof_string>, lens: <proof_string>}}`
3. push file to ipfs with web3 storage
4. take content_id from 3. and store `{address: cid}` on gundb

## add proofs (app 1)
1. proof generated somehow (sign a message with wallet) save signature as `proof_string` in IPFS storage json
2. in order to prove something: pull `cid` from gundb, pull file, edit with new proof string, push to new IPFS reference, update `cid` in GunDB

### twitter
1. button "prove your twitter", type in username
2. sign a message containing some nonce and their twitter username and their address
3. generate second message for them to tweet with their address, our project name and the signature
4. ask them to copy the tweet url and post it in the dashboard
5. check for tweet
    - *v1* check address + username
    - *v2* verify signature somehow? smt else?
6. show that twitter is proved 
### github
1. ~~later~~
### linkedn
1. ~~later~~
### ssh
1. ~~later~~

## verify proofs (app 2)