from zope.interface import Interface
from zope import schema

from collective.contentrules.runscript import runscriptMessageFactory as _


class IParamValuePair(Interface):
    name = schema.TextLine(title=_(u"Name"), required=True)
    value = schema.TextLine(title=_(u"Value"), required=True)


class IRunScriptAction(Interface):
    """Definition of the configuration available for a runscript action"""

    script = schema.TextLine(
        title=_(u"Script"),
        description=_(u"The script"),
        required=True
    )

    parameters = schema.List(
        title=_(u'Parameter list'),
        description=_(u"A list of parameters you wish to pass to the script. "
                      u"Place each param=value pair on a new line. "
                      u"Also, the system will evaluate the value of the parameter. "
                      u"If it fails to evaluate the value, then the value will be str type."),
        default=[],
        value_type=schema.TextLine(title=_(u"Parameter")),
        required=False
    )

    include_contentrule_context = schema.Bool(
        title=_("Include the context that this contentrule applies to as a parameter."),
        description=_(u"If checked, assign the context as the contentrule_context parameter"),
        required=False
    )

    fail_on_script_not_found = schema.Bool(
        title=_("Fail on script not found"),
        description=_(u"Raise exception if script can't be traversed to from object."),
        required=False
    )

    restricted_traverse = schema.Bool(
        title=_("Perform permission verification on script"),
        description=_("If checked, tries to do a restricted traversal to the script."),
        required=False
    )