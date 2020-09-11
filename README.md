# xmlimporter

The xmlimporter in this repo has a connection to Amelie.

From the code, it seems that the python script retrieves XML objects from a file, the properties of this object are:

'Siemens.SSF.Common.CompletedDate'

'System.CreatedDate' 

'System.Title'

'Sytem.Description'

'System.State'

'System.AssignedTo'

'System.WorkItemType'

'System.CreatedBy'

After retrieving the value of each property, this script connects to a MongoDB database and updates this object base on its ID.
