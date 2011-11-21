from django.template import Library, Node, TemplateSyntaxError

from django_pusher.push import pusher


register = Library()


class PusherKeyNode(Node):
    def __init__(self, vars):
        self.vars = vars

    def render(self, context):
        args = []
        for var in self.vars:
            args.append(var.resolve(context, True))
        return pusher.make_key("".join(args))


@register.tag
def pusher_key(parser, token):
    bits = token.split_contents()[1:]
    if len(bits) < 1:
        raise TemplateSyntaxError("'pusher_key' statement requires at least one argument")
    return PusherKeyNode([parser.compile_filter(bit) for bit in bits])
