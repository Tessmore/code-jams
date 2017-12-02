<?php

function is_palindrome($number) {
  $digits = str_split($number);
  $length = count($digits);
  $N      = .5 * ($length + .5);
 
  for($i=0; $i<$N; $i++, $length--)
    if ($digits[$i] !== $digits[$length-1])
      return 0;
  
  return 1;
}

$file   = 'C-small-attempt0';
$input  = explode("\n", file_get_contents($file . '.in'));
$output = array();

$T = (int) array_shift($input);

for ($j=0; $j<$T; $j++) {
  $count = 0;
  list($A, $B) = explode(' ', array_shift($input));

  for ($i=$A; $i<=$B; $i++)
    $count += is_palindrome($i) && is_palindrome(sqrt($i));
    
  $output[] = sprintf('Case #%d: %d', $j+1, $count); 
}

file_put_contents($file . '.out', implode("\n", $output));

print "Done";