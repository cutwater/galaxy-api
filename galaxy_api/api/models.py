from django.db import models

from galaxy_api.auth import models as auth_models


__all__ = (
    'Namespace',
    'NamespaceLink',
    'Collection',
)


class Namespace(models.Model):
    """
    A model representing Ansible content namespace.

    Fields:
        name: Namespace name. Must be lower case containing only alphanumeric
            characters and underscores.
        company: Optional namespace owner company name.
        email: Optional namespace contact email.
        avatar_url: Optional namespace logo URL.
        description: Namespace brief description.
        resources_page: Namespace resources page in markdown format.
        resource_page_html: HTML representation of a resources page.

    Relations:
        owners: Reference to namespace owners.
        links: Reference to related links.

    """

    # Fields

    name = models.CharField(max_length=64, unique=True, editable=False)
    company = models.CharField(max_length=64, blank=True)
    email = models.CharField(max_length=256, blank=True)
    avatar_url = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=256, blank=True)

    # TODO(cutwater): Consider moving to a standalone model
    resources_page = models.TextField(blank=True)
    resources_page_html = models.TextField(blank=True, editable=False)

    # References
    owners = models.ManyToManyField(auth_models.Tenant, related_name='namespaces')


class NamespaceLink(models.Model):
    """
    A model representing a Namespace link.

    Fields:
        name: Link name (e.g. Homepage, Documentation, etc.).
        url: Link URL.

    Relations:
        namespace: Reference to a parent namespace.
    """

    # Fields
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=256)

    # References
    namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE, related_name='links')


class Collection(models.Model):
    """
    A model representing Ansible content collection.

    Fields:
        name: Collection name. Must be lower case containing
            only alphanumeric characters and underscores.
        remote_id: Collection ID in remote database.

    Relations:
        namespace: Reference to a collection Namespace.
    """

    # Fields
    name = models.CharField(max_length=64, editable=False)
    remote_id = models.UUIDField(unique=True, editable=False)

    quality_score = models.FloatField(null=True, editable=False)

    # References
    namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE, editable=False)

    class Meta:
        unique_together = (
            'namespace',
            'name',
        )
