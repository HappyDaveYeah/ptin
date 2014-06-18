/**
 * Bootstrap
 * (sails.config.bootstrap)
 *
 * An asynchronous bootstrap function that runs before your Sails app gets lifted.
 * This gives you an opportunity to set up your data model, run jobs, or perform some special logic.
 *
 * For more information on bootstrapping your app, check out:
 * http://links.sailsjs.org/docs/config/bootstrap
 */

module.exports.bootstrap = function(cb) {

  // It's very important to trigger this callack method when you are finished
  // with the bootstrap!  (otherwise your server will never lift, since it's waiting on the bootstrap)
	var dummyApps = [
		{
			"name": "Bus",
			"cat": "Traffic",
			"icon": "bus.png",
			"dir": "bus",
			"file_name": "bus.py"
		},
		{
			"name": "Lightning",
			"cat": "Energy",
			"icon": "lightning.png",
			"dir": "lightning",
			"file_name": "lightning.py"
		},
		{
			"name": "Cams",
			"cat": "Security",
			"icon": "cams.png",
			"dir": "cams",
			"file_name": "cams.py"
		},
		{
			"name": "Factory",
			"cat": "Productivity",
			"icon": "factory.png",
			"dir": "factory",
			"file_name": "factory.py"
		},
		{
			"name": "Health",
			"cat": "Security",
			"icon": "health.png",
			"dir": "health",
			"file_name": "health.py"
		},
		{
			"name": "Store",
			"cat": "Productivity",
			"icon": "store.png",
			"dir": "store",
			"file_name": "store.py"
		},
		{
			"name": "Lab",
			"cat": "Productivity",
			"icon": "lab.png",
			"dir": "lab",
			"file_name": "lab.py"
		}
	];

    App.count().exec(function(err, count) {
        if(err) {
            sails.log.error('App already have data.');
            return cb(err);
        }
        if(count == 0) App.create(dummyApps);
    });
	
	/* Stats {enabled, installed} per defecte de les apps
	Navi.findOne(1).exec(function(err, navi) {
		if(err) {
            sails.log.error('Error al associar');
            return cb(err);
        }

		// Queue up a record to be inserted into the join table
		navi.installed.add(1);
		navi.enabled.add(1);
		navi.installed.add(2);
		navi.installed.add(4);
		navi.installed.add(6);
		navi.enabled.add(6);

		// Save the user, creating the new associations in the join table
		navi.save(function(err) {});
	});
	*/
	
	// Setting up els logs per defecte
	Log.destroy().exec(function (){});
	Log.create({timestamp:'1401019205.93', levelno: 50, message: "Server Not Responding", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1400919205.12', levelno: 20, message: "Server Rebooted", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1400719205.36', levelno: 50, message: "Server Crashed", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1399723205.61', levelno: 20, message: "Bus - Application Stopped", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1399723105.26', levelno: 20, message: "Bus - Application Started", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1399713205.98', levelno: 50, message: "Server Not Responding", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1399693921.21', levelno: 30, message: "New Updates", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1399623205.74', levelno: 20, message: "Server Rebooted", loggedBy: 1}).exec(function (){});
	Log.create({timestamp:'1397223205.11', levelno: 50, message: "Server Crashed", loggedBy: 1}).exec(function (){});
	
	//App.create({name:"Turtle", cat: "Proof", icon: "turtle.png", dir: "turtle", file_name: "turtle.py"}).exec(function (){});

	/*
	Log.find().exec(function(err, logs) {
		if(err) {
			sails.log.error('Error al associar');
			return cb(err);
		}
		var log;
		while (logs.length) {
			log = logs.pop();
			log.loggedBy = 1;
			log.save(function(err) {});
		}
		
	});
	*/

cb();
};
