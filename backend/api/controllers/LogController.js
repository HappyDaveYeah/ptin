/**
 * LogController
 *
 * @description :: Server-side logic for managing logs
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {
	clearlogs: function(req, res) {
		if (req.param('loglevel') == "all") {
			Log.destroy({loggedBy:req.param('id')}).exec(function (){});
		}
		else {
			Log.destroy({loggedBy:req.param('id'), levelno:req.param('loglevel')}).exec(function (){});
		}
		res.json(200);
    },
	getlogs: function(req, res) {
		Log.find().where({'loggedBy':req.param('id')}).sort('timestamp ASC').exec(function (err, logs) {
			if (err) return res.send(err,500);
			if (!logs) return res.send("No Navi with that id exists!", 404);
			return res.json(logs);
		});
    },
	logging: function(req, res) {
		var values = req.params.all()
		delete values.id;
		
		switch (values.event) {
				case "install":
					Navi.findOne(values.idNavi).populate('installed').exec(function (err, navi){
						navi.installed.add(values.extra.idApp);
						navi.save(function(err) {});
					});
					break;
				case "remove":
					Navi.findOne(values.idNavi).populate('enabled').populate('installed').exec(function (err, navi){
						navi.enabled.remove(values.extra.idApp);
						navi.installed.remove(values.extra.idApp);
						navi.save(function(err) {});
					});
					break;
				case "start":
					Navi.findOne(values.idNavi).populate('enabled').exec(function (err, navi){
						navi.enabled.add(values.extra.idApp);
						navi.save(function(err) {});
					});
					break;
				case "stop":
					Navi.findOne(values.idNavi).populate('enabled').exec(function (err, navi){
						navi.enabled.remove(values.extra.idApp);
						navi.save(function(err) {});
					});
					break;				
		}
		Log.create({timestamp: values.timestamp, levelno: values.levelno, message: values.message, loggedBy: values.idNavi}).exec(function (err,created){});
		//sails.log.info(values);
		return res.ok();
	}
};

