## Controller Python Script "tag_after_contentrule_context"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=contentrule_context
##title=Tag after the contentrule context
##
#Conditionally adds the parent's title as a tag in the context's subject field.
#Recursively tests whether title_as_tag property is set on each part of the object's parent's
#path and adds that part's title as a tag on the object.

pTag = contentrule_context.Title()
keys = context.Subject()
if pTag not in keys:
    keys += (pTag,)
    context.setSubject(keys)
    context.reindexObject(idxs=['subject'])
