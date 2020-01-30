const express = require('express');
const router = express.Router();

// router.get('/',(req, res, next) => {
//     res.status(200).json({
//         message: 'Handling GET requests to /usermanagement' 
//     });
// });


router.post('/', (req, res, next) => {
    res.status(200).json({
        message: 'Handling POST requests to /usermanagement' 
    });
});

router.patch('/:userid', (req, res, next) => {
    res.status(200).json({
        message: 'Updated User Details!' 
    });
});

router.delete('/:userid', (req, res, next) => {
    res.status(200).json({
        message: 'Deleted User Details!' 
    });
});



//to get a single user id
router.get('/:userid',(req, res, next) => {
    const id = req.params.userid;
    
    if(id === 'id_fetched_from_DB')
    {
        res.status(200).json({
        message: 'Fetching Details of the Current User',
        //returning the id
        id: id 
        });
    } else{
        res.status(200).json({
            message: 'Incorrect UserId entered',
            
            });
         }
    
});

module.exports =  router;

