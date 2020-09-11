# xmlimporter

The xmlimporter in this repo has a connection to Amelie.

From the code, it seems that the python script retrieve XML objects from a file, the properties of this object are:

'Siemens.SSF.Common.CompletedDate'
'System.CreatedDate' 
'System.Title'
'Sytem.Description'
'System.State'
'System.AssignedTo'
'System.WorkItemType'
'System.CreatedBy'

After retrieve the value of each property, this script connect to a MongoDB database and update this object base on its ID.
