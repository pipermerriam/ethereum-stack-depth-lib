# Ethereum Stack Depth checker

An ethereum library that provides a utility function that can be used to check
whether it is possible to increase the stack depth by a specified amount.

This can help prevent a certain type of attack where a caller can cause a
function to fail if she knows that the function performs an operation which
increases the stack depth as well as knowing what depth the function is going
to be called at.

She can then artificially increase the stack depth prior to entering into the
function call, and the targeted function will fail due to exceeding the maximum
stack depth (1024)

Credit goes to Martin Holst Swende [@mhswende](https://twitter.com/mhswende)
for teaching me about this attack vector.


## API

**StackDepthLib.check_depth(address me, uint depth) returns (bool)**

Parameters:

* `self`: This is the address of the deployed `StackDepthLib` library.  This is
  necessary because the depth checking requires recursion and libraries are
  unable to determine their own addresses since they operate on other libraries
  storage.
* `depth`: Integer stack depth increase you would like to check.

Returns a boolean as to whether the depth increase was successful or not.

This will use approximately 390 gas per stack depth level.  The library
reserves 400 gas per level, so if you want to check for 100 levels, it will
cost around 40,000 gas.
