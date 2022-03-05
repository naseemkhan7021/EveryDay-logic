<?php
function pageCount(int $page = null, int $lenth = null)
{
     # code...
     $front = intdiv($page, 2);
     if ($lenth % 2 == 1) {
          $back = intdiv(($lenth - $page), 2);
     } else {
          $back = intdiv(($lenth - $page + 1), 2);
     };
     return min($front, $back);
}
$page = 5;
$lenth = 4;
echo pageCount($page, $lenth);