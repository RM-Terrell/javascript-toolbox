//Encapsulation of props that an object links to.
//A class is like a blue print, describing the object to be created.
//A prototype is a working object instand, where objects inherit from other objects. Allows for object composition.

var Task = function(name){
  this.name = name;
  this.completed = false;
}
Task.prototype.complete = function(){
  console.log('completing task: ' + this.name);
  this.completed = true;
}
Task.prototype.save = function(){
  console.log('saving task: ' + this.name);
}

var task1 = new Task('create constructor demo');

task1.complete();
