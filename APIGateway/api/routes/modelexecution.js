const express = require('express');
const router = express.Router();

router.get('/',(req, res, next) => {
    res.status(200).json({
        message: 'Handling GET requests to /modelexecution' 
    });
});


router.post('/', (req, res, next) => {
    res.status(200).json({
        message: 'Handling POST requests to /modelexecution' 
    });
});

module.exports =  router;