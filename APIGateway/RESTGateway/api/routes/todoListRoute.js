'use strict';
module.exports = function(app) {
  console.log("inside route")
  // var DataRetrievalController = require('../controllers/DataRetrievalController');
  var UserManagementController = require('../controllers/UserManagementController');
  // var SessionManagementController = require('../controllers/SessionManagementController')
  // todoList Routes
  // app.route('/getWeatherData')
    // .get(DataRetrievalController.getWeatherData);

    
    
  app.route('/authenticate')
    .post(UserManagementController.login);

  // app.route('/register')
    // .post(UserManagementController.register); 
    
    // app.route('/user_dashboard')
    // .get(UserManagementController.user_details); 
  // app.route('/token/validate')
    // .post(SessionManagementController.validateToken)
}