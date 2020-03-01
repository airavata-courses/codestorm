'use strict';
module.exports = function(app) {
  console.log("inside route")
  var DataRetrievalController = require('../controllers/DataRetrievalController');
  var UserManagementController = require('../controllers/UserManagementController');
  var ModelExecutionController = require('../controllers/ModelExecutionController');
  var PostProcessingController = require('../controllers/PostProcessingController');
  var SessionManagementController = require('../controllers/SessionManagementController');
  

  // var SessionManagementController = require('../controllers/SessionManagementController')
  // todoList Routes
  app.route('/getWeatherData')
    .post(DataRetrievalController.getWeatherData);

  app.route('/modelexecution')
    .get(ModelExecutionController.getModelExecutionStatus);

  app.route('/authenticate')
   .post(UserManagementController.login);

   app.route('/register')
     .post(UserManagementController.register); 

  app.route('/postprocessing')
    .get(PostProcessingController.postprocessing); 

  app.route('/user/me')
     .get(UserManagementController.loadcurrentuser);
    
    // app.route('/user_dashboard')
    // .get(UserManagementController.user_details); 
  app.route('/sendsessiondata')
    .post(SessionManagementController.sendsessiondata);
}