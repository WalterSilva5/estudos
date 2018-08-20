<?php
require "vendor/Rain/autoload.php";
// namespace
use Rain\Tpl;
// config
$config = array(
    "tpl_dir"       => "tpl",
    "cache_dir"     => "cache/",
);
Tpl::configure( $config );

// create the Tpl object
$tpl = new Tpl;
// assign a variable
$tpl->assign( "name", "Walter" );
// assign an array
$tpl->assign( "Exemplo", "Sobrenome");
// draw the template
$tpl->draw( "index" );
?>