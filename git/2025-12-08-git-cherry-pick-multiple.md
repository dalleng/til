# Cherry-pick multiple commits

- If the commits are contiguous, you can use `git cherry-pick <start>..<end>`.  
  The left side of the range is exclusive, so if you want `<start>` to be included, you need to use `^`, like this:  
  `git cherry-pick <start>^..<end>`.

  Example:  
  `git cherry-pick 4775d641284769b2f5d7cd1e107621cdc3712c9c^..c98a582cc7edae01cb0845f00adda965b8f3f8c3`

- If the commits are not contiguous, list them explicitly:  
  `git cherry-pick <commit1> <commit2> ... <commitN>`.