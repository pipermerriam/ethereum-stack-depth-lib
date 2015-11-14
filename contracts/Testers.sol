import "libraries/StackDepthLib.sol";


contract TestDepth {
        address sdl;

        function set_sdl(address _sdl) public {
                sdl = _sdl;
        }

        function test_depth(uint n, uint d) constant returns (bool) {
                if (n > 0) {
                        TestDepth me = TestDepth(address(this));
                        return me.test_depth(n - 1, d);
                }
                else {
                        return StackDepthLib.check_depth(sdl, d);
                }
        }
}
