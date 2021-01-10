# Concurrency and Parallelism

Came across a really simple and good explanation of the difference between
concurrency and parallelism in Rob Pike's talk ["Concurrency is not Parallelism"][1].

From Rob Pike's slides:

> Concurrency is about dealing with a lot of things at once.
> Parallelism is about doing a lot of things at once.

So I think the main takeway of the talk is that for either concurrency
or parallelism you actually need to think how to decompose a problem into
independent subtasks. Concurrent decomposition.

After decomposing the problem, actually having concurrency or parallelism
boils down to how subtasks are scheduled. So, for the case of a multicore
cpu you can actually schedule subtasks to run different subtasks at once
so you'll be doing simultaneous work and thus achieving parallelism. For
the case of a single core cpu you could execute subtasks one at a time
but context switch between them, thus making progress on all of them
in the same period of time achieving concurrency but not parallelism.

[1]:https://www.youtube.com/watch?v=qmg1CF3gZQ0
