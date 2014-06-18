/**
* Navi.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {

  attributes: {
  
	location: {
			type: 'string'
	},
	installed: {
		collection: 'app',
		via: 'installedBy',
		dominant: true
	},
	enabled: {
		collection: 'app',
		via: 'enabledBy',
		dominant: true
	}
  }
};

