<?
class Player{
  private $name;
  private $level;

  // constructor
  function __construct($name, $level){
    $this->name = $name;
    $this->level = $level;
  }

  // getter
  function getName(){
    return $this->name;
  }

  // setter
  function setName($name){
    $this->name = $name;
  }
}

$player = new Player('joost', 20);