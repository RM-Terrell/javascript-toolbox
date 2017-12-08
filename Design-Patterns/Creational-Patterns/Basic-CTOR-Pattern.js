// Similar to creating a new instance of class if thought about in a C#, Java context
// "new" keyword

//Example constructor function
function ObjectName(param1, param2){
  this.param1 = param1;
  this.param2 = param2;
  this.toString = function(){
    return this.param1 + ' ' + this.param2;
  }
  //implicitly returns 'this' at the end
}
