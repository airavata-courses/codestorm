const express = require('express');

const app =  express();

const userManagementRoutes = require('./api/routes/usermanagement');

const sessionManagementRoutes = require('./api/routes/sessionmanagement');

const dataRetrievalRoutes = require('./api/routes/dataretrieval');

const modelExecutionRoutes = require('./api/routes/modelexecution');

const postProcessingRoutes = require('./api/routes/postprocessing');

app.use('/usermanagement', userManagementRoutes);

app.use('/sessionmanagement', sessionManagementRoutes);

app.use('/dataretrieval', dataRetrievalRoutes);

app.use('/modelexecution', modelExecutionRoutes);

app.use('/postprocessing', postProcessingRoutes);

// app.use((req,res, next)=>{
//         message: 'It works!'
//     });
// });

module.exports = app;

