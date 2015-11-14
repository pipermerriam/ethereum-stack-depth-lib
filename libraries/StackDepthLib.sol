library StackDepthLib {
        uint constant GAS_PER_DEPTH = 425;

        function check_depth(address me, uint n) constant returns (bool) {
                if (n == 0) return true;
                uint gas = GAS_PER_DEPTH * n;
                if (gas > msg.gas) return false;
                return me.callcode.gas(gas)(bytes4(sha3("__dig(address,uint256)")), me, n - 1);
        }

        function __dig(address me, uint n) constant returns (bool) {
                if (n == 0) return true;
                if (!me.callcode(bytes4(sha3("__dig(address,uint256)")), me, n - 1)) {
                        throw;
                }
        }
}
