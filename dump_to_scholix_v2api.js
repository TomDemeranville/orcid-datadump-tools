//dump to scholix
//transforms the datadump into a scholix like format.
db.orciddump.find().forEach(function(record) {
	if (record["activities-summary"]["works"]["group"] != null){
            record["activities-summary"]["works"]["group"].forEach(
                function(group){
					if (group["external-ids"] != null && group["external-ids"]["external-id"] !=null){
					    group["external-ids"]["external-id"].forEach(
					        function(id){
					        	//group?
					        }
					    );
					}
                    group["work-summary"].forEach(
                        function(work){
                            if (work["external-ids"] != null && work["external-ids"]["external-id"] !=null){
                                work["external-ids"]["external-id"].forEach(
                                    function(id){
							        	var out = {};
							        	out.link_publisher = {};
							        	out.link_publisher.name = work.source["source-name"].value;
								        out.link_publisher.id = {};
								        if (work.source["source-orcid"]){
								        	out.link_publisher.id.value = work.source["source-orcid"].uri;
								        	out.link_publisher.id.type = "orcid";
								        }else if (work.source["source-client-id"]){
								        	out.link_publisher.id.value = work.source["source-client-id"].uri;
								        	out.link_publisher.id.type = "orcid-client";
								        }
							        	out.link_provider = {};
							        	out.link_provider.name = "orcid";
							        	out.link_provider.id = {};
							        	out.link_provider.id.type = "grid.ac";
							        	out.link_provider.id.value = "grid.455335.1";
							        	out.source_object = {};
							        	if (record.person.name["credit-name"])
								        	out.source_object.name = record.person.name["credit-name"].value;
								        else if (record.person.name["given-names"]){
								        	out.source_object.name =record.person.name["given-names"].value +" "+record.person.name["family-name"].value;
								        }
							        	out.source_object.id = {};
							        	out.source_object.id.value = record["orcid-identifier"].uri;
							        	out.source_object.id.schema = "orcid";
							        	out.source_object.id.type = "person";
							        	out.target_object = {};
							        	out.target_object.name = work.title.title.value;
							        	out.target_object.id = {};
							        	out.target_object.id.value = id["external-id-value"];
							        	out.target_object.id.schema = id["external-id-type"];
							        	out.target_object.name = work.title.title.value;
							        	out.target_object.id.type = work.type;
							        	out.relationship_type = "relatedTo";
							        	out._id = work["put-code"];
							        	db.scholix.save(out);
                                    }
                                );
                            }
                        }
                    );

                }
            );
        }
});