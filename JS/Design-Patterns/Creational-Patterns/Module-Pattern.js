//Module patter creates a "toolbox" of functions
//Allows us to be able to create a functional equiv of private variables


var repo = function(){
  return{
    get: function(id){
      //stuff for getting items from a database
    }
  }
}
module.exports = repo();
//can now be used by doing the following
repo.get(1);
