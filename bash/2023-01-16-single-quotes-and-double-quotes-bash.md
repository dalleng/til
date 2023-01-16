# Difference between single and double quotes in bash.

Content inside single quotes is interpreted literally without string interpolation, while content inside
double quotes is subject to string interpolation. See:

```bash
bash-3.2$ echo '$a'
$a
bash-3.2$ echo "$a"
10
```

[Source](https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash#:~:text=If%20you're%20referring%20to,the%20value%20of%20the%20variable.&text=Save%20this%20answer.,-Show%20activity%20on)