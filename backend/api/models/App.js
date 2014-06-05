/**
 * App
 *
 * @module      :: Model
 * @description :: A short summary of how this model works and what it represents.
 * @docs		:: http://sailsjs.org/#!documentation/models
 */

module.exports = {

  attributes: {

  	name: {
        type: 'string',
        required: true
    },
    cat: {
        type: 'string',
        required: true
    },
    icon: {
        type: 'string',
        required: true
    },
    dir: {
        type: 'string',
        required: true
    },
    file_name: {
        type: 'string',
        required: true
    }
    
  }

};
