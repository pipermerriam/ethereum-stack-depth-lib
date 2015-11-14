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

        modifier require_stack_depth(uint16 depth) {
                if (depth > 1023) throw;
                if (!StackDepthLib.check_depth(sdl, depth)) throw;
                _
        }

        function test_requires_depth(uint16 drill_to) constant returns (bool) {
                if (drill_to > 0) {
                        TestDepth me = TestDepth(address(this));
                        return me.test_requires_depth(drill_to - 1);
                }
                return requires_depth();
        }

        function requires_depth() constant require_stack_depth(1000) returns (bool) {
                return true;
        }
}
