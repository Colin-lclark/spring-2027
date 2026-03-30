# Note 27

## PHP

PHP is a general-purpose scripting language geared towards server-side web
development. The language typing discipline is *dynamic* and *weak*. For PHP,
this discipline means that type checking is performed at runtime (as the program
executes) and type annotation is optional. If you do not add type annotation,
the type of a variable will inherit the type of the value assigned to it.

### Your first PHP program

Create a file called `hello.php` in `/Applications/XAMPP/htdocs/tree` with the
following content:

```php
<?php
  echo 'Hello world!';
?>
```

Then point your web browser to URL `localhost/tree/hello.php` to run this
program.

Note that all PHP statements must end with a semicolon (`;`).

### Types

PHP supports the following built-in types:

* Booleans:
  * `TRUE`, `FALSE` (case insensitive)
* Integers:
  * `0`, `123_456_789`
  * `017` (octal), `0x17` (hexadecimal), `0xb11011` (binary)
* Floating point numbers:
  * `3.1415`, `1.2e-3`, `1.2E-3`, `1_234.567`
* Strings:
  * Single quoted:
    * `'hello'`
    * `'a string with a double quote\' inside'`
    * `'a string with a backslash \\ inside'`
  * Double quoted:
    * `"hello"`
    * Note the difference between `'hello\n'` and `"hello\n"`

### Variables

Variable identifiers must start with a dollar sign (`$`).

```php
<?php
  $i = 0;
  $n = 123.4;
  $v = TRUE;
  $f_name = 'Ada';
  $l_name = 'Lovelace';
?>
```

Type annotation is optional in PHP. The type assigned a variable will depend on
the value assigned to it. Here `$i` "becomes" an integer when initialized with
an integer literal; `$n` "becomes" a floating point when initialized with a
floating point literal.

### Constants

A constant identifier does not start with a dollar sign and by convention it is
all uppercase. A constant is given a value with the `define()` function.

```php
<?php
  define('PI', 3.1415);
  define('ZERO_VALUE', 0);
  define('NAME', 'Archer');
  echo NAME;
?>
```

### Some operators

PHP and C share many of the same operators. Of note, PHP uses dot (`.`) as the
string concatenation operator.

### `Hello world` again

Here is the hello world program again but slightly modified.

```php
<?php
  echo 'Hello, World!<br>';
?>
```

Since the output of processing a PHP program is an HTML document, one uses 
`<br>` to indicate a newline rather than `\n`.

### `Hello world` embedded in an HTML document
Here is a simple hello world program embedded in an HTML document.

```php
<!DOCTYPE html>
<html>
  <head>
    <title>PHP 'Hello, World!' program</title>
  </head>
  <body>
    <?php
      echo '<p>Hello, World!</p>';
    ?>
  </body>
</html>
```

### The while loop

```php
<?php
  $i = 0;
  while ($i < 4) {
    echo $i . '<br>';
    ++$i;
  }
?>
```

### Arrays

```php
<?php
  $a = array('a', 'aardvark', 'abaci', 'aback');
  $i = 0;
  while ($i < 4) {
    echo $a[$i] . '<br>';
    ++$i;
  }
?>
```

PHP also supports associative arrays.

### Accessing a database

Here is some code to open a connection to a database.

```php
<?php
  define('DB_USER', 'registrar');
  define('DB_PASSWORD', 'reg');
  define('DB_HOST', 'localhost');
  define('DB_NAME', 'registrar');

  ($dbc = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD,
                         DB_NAME))
    || die('Could not connect to MariaDB: '
           . mysqli_connect_error());
?>
```

Here is a statement to close the connection.

```php
<?php
  mysqli_close($dbc);
?>
```

### File inclusion

You can include another PHP file with the function `require()`. For example:

```php
<?php
  require('./connect.php');
?>
```

### Querying a database

```php
<?php
  require('./connect.php');

  $query = 'SELECT id, name FROM course LIMIT 10';
  $response = mysqli_query($dbc, $query);
  if ($response) {
    echo '<table
          <tr><td><b>ID</b></td>
              <td><b>Name</b></td><tr>';

    while ($row = mysqli_fetch_array($response)) {
      echo     	'<tr><td>' .
      $row['id']   . '</td><td>' .
      $row['name'] . '</td>';
      echo '</tr>';
    }

    echo '</table>';
  }
  else {
    echo 'Couldn\'t issue database query: ' . mysqli_error($dbc);
  }

  mysqli_close($dbc);
?>
```
