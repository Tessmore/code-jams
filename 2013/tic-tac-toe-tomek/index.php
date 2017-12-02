<?php

$file   = 'A-small-attempt1';
$input  = explode("\n", file_get_contents($file . '.in'));
$output = array();

$x_solutions = array(
  'XXXX',
  'XXXT',
  'XXTX',
  'XTXX',
  'TXXX'
);

$o_solutions = array(
  'OOOO',
  'OOOT',
  'OOTO',
  'OTOO',
  'TOOO'
);

$T = (int) array_shift($input);

for ($j=0; $j<$T; $j++) {
  $lines = array(
    str_split( ($a = trim(array_shift($input))) ),
    str_split( ($b = trim(array_shift($input))) ),
    str_split( ($c = trim(array_shift($input))) ),
    str_split( ($d = trim(array_shift($input))) )
  );
  
  $str = $a.$b.$c.$d;
        
  array_shift($input);
   
  $board = array(
    implode('', $lines[0]),
    implode('', $lines[1]),
    implode('', $lines[2]),
    implode('', $lines[3]),

    $lines[0][0] . $lines[1][1] . $lines[2][2] . $lines[3][3], 
    $lines[3][0] . $lines[2][1] . $lines[1][2] . $lines[0][3], 
    
    $lines[0][0] . $lines[1][0] . $lines[2][0] . $lines[3][0], 
    $lines[0][1] . $lines[1][1] . $lines[2][1] . $lines[3][1], 
    $lines[0][2] . $lines[1][2] . $lines[2][2] . $lines[3][2], 
    $lines[0][3] . $lines[1][3] . $lines[2][3] . $lines[3][3]
  );
  
  $found_solution = false;
  
  foreach ($x_solutions as $s) {
    if (in_array($s, $board)) {
      $found_solution = true;
      
      $output[] = sprintf('Case #%d: %s', $j+1, 'X won');
      break;
    }
  }

  if (! $found_solution)
    foreach ($o_solutions as $s) {
      if (in_array($s, $board)) {
        $found_solution = true;

        $output[] = sprintf('Case #%d: %s', $j+1, 'O won');
        break;
      }
    }
  
  if (! $found_solution) {    
    if (strpos($str, '.') === FALSE)
      $output[] = sprintf('Case #%d: %s', $j+1, 'Draw');
    else
      $output[] = sprintf('Case #%d: %s', $j+1, 'Game has not completed');
  }
}

file_put_contents($file . '.out', implode("\n", $output));

print "Done";