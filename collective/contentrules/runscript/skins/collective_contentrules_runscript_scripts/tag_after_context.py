## Script (Python) "tag_after_context"
##title=Tag after context's title
##bind container=container
##bind context=context

#Adds the parent's title as a tag in the context's subject field.

pTag = context.Title()
keys = context.Subject()
if pTag not in keys:
    keys += (pTag,)
    context.setSubject(keys)
    context.reindexObject(idxs=['subject'])