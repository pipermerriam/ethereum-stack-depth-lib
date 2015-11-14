library StackDepthLib {
        // This will probably work with a value of 390 but no need to cut it
        // that close in the case that the optimizer changes slightly or
        // something causing that number to rise slightly.
        uint constant GAS_PER_DEPTH = 400;

        function check_depth(address self, uint n) constant returns (bool) {
                if (n == 0) return true;
                return self.call.gas(GAS_PER_DEPTH * n)(0x21835af6, n - 1);
        }

        function __dig(uint n) constant returns (bool) {
                if (n == 0) return true;
                if (!address(this).callcode(0x21835af6, n - 1)) throw;
        }
}
