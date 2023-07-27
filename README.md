# PyWaku
Waku bindings for Python.

## Dependencies
* Waku v2

## Development

#### Start a nim-based Waku node 
```bash
docker run --rm -p 127.0.0.1:8545:8545/tcp --name nwaku statusteam/nim-waku:v0.18.0 --dns-discovery=true --rpc-address=0.0.0.0 --dns-discovery-url=enrtree://AOGECG2SPND25EEFMAJ5WF3KSGJNSGV356DSTL2YVLLZWIV6SAYBM@prod.waku.nodes.status.im --discv5-discovery=true
```

#### Sample request
```bash
curl -d '{"jsonrpc":"2.0", "method": "get_waku_v2_debug_v1_info", "params": [], "id": 1}' -H 'Content-Type: application/json' localhost:8545
```

# Docs
[VAC RFC](https://rfc.vac.dev/)
