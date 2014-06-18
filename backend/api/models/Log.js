/**
* Log.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {

  attributes: {
	timestamp: {
		type: 'string',
		required: true
	},
	levelno: {
		type: 'integer',
		required: true
	},
	message: {
		type: 'string',
		required: true
	},
	loggedBy: {
		model: 'navi'
	}
  }
};

