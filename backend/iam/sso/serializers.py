from allauth.socialaccount.providers.saml.provider import SAMLProvider
from rest_framework import serializers

from settings.models import GlobalSettings
from .models import SSOSettings

from core.serializers import BaseModelSerializer


class SSOSettingsReadSerializer(BaseModelSerializer):
    name = serializers.CharField(read_only=True, source="get_name")
    provider = serializers.CharField(read_only=True, source="get_provider_display")
    settings = serializers.CharField(read_only=True)

    class Meta:
        model = SSOSettings
        exclude = ["value"]


class SSOSettingsWriteSerializer(BaseModelSerializer):
    provider = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    provider_id = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    client_id = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    provider_name = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.name",
    )
    attribute_mapping_uid = serializers.ListField(
        child=serializers.CharField(
            required=False,
            allow_blank=True,
            allow_null=True,
        ),
        required=False,
        allow_null=True,
        source="settings.attribute_mapping.uid",
    )
    attribute_mapping_email_verified = serializers.ListField(
        child=serializers.CharField(
            required=False,
            allow_blank=True,
            allow_null=True,
        ),
        required=False,
        allow_null=True,
        source="settings.attribute_mapping.email_verified",
    )
    attribute_mapping_email = serializers.ListField(
        child=serializers.CharField(
            required=False,
            allow_blank=True,
            allow_null=True,
        ),
        required=False,
        allow_null=True,
        source="settings.attribute_mapping.email",
    )
    idp_entity_id = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.idp.entity_id",
    )
    metadata_url = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.idp.metadata_url",
    )
    sso_url = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.idp.sso_url",
    )
    slo_url = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.idp.slo_url",
    )
    x509cert = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.idp.x509cert",
    )
    sp_entity_id = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.sp.entity_id",
    )
    allow_repeat_attribute_name = serializers.BooleanField(
        required=False,
        source="settings.advanced.allow_repeat_attribute_name",
    )
    allow_single_label_domains = serializers.BooleanField(
        required=False,
        source="settings.advanced.allow_single_label_domains",
    )
    authn_request_signed = serializers.BooleanField(
        required=False,
        source="settings.advanced.authn_request_signed",
    )
    digest_algorithm = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.advanced.digest_algorithm",
    )
    logout_request_signed = serializers.BooleanField(
        required=False,
        source="settings.advanced.logout_request_signed",
    )
    logout_response_signed = serializers.BooleanField(
        required=False,
        source="settings.advanced.logout_response_signed",
    )
    metadata_signed = serializers.BooleanField(
        required=False,
        source="settings.advanced.metadata_signed",
    )
    name_id_encrypted = serializers.BooleanField(
        required=False,
        source="settings.advanced.name_id_encrypted",
    )
    reject_deprecated_algorithm = serializers.BooleanField(
        required=False,
        source="settings.advanced.reject_deprecated_algorithm",
    )
    reject_idp_initiated_sso = serializers.BooleanField(
        required=False,
        source="settings.advanced.reject_idp_initiated_sso",
    )
    signature_algorithm = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        source="settings.advanced.signature_algorithm",
    )
    want_assertion_encrypted = serializers.BooleanField(
        required=False,
        source="settings.advanced.want_assertion_encrypted",
    )
    want_assertion_signed = serializers.BooleanField(
        required=False,
        source="settings.advanced.want_assertion_signed",
    )
    want_attribute_statement = serializers.BooleanField(
        required=False,
        source="settings.advanced.want_attribute_statement",
    )
    want_message_signed = serializers.BooleanField(
        required=False,
        source="settings.advanced.want_message_signed",
    )
    want_name_id = serializers.BooleanField(
        required=False,
        source="settings.advanced.want_name_id",
    )
    want_name_id_encrypted = serializers.BooleanField(
        required=False,
        source="settings.advanced.want_name_id_encrypted",
    )

    class Meta:
        model = SSOSettings
        exclude = ["value"]

    def update(self, instance, validated_data):
        # if validated_data.get("provider") == "saml":
        #     settings = self.build_saml_settings(validated_data)
        #     validated_data["settings"] = settings
        settings_object = GlobalSettings.objects.get(name=GlobalSettings.Names.SSO)
        settings_object.value = validated_data
        # print(settings_object.value)
        settings_object.save()
        return instance

    def build_saml_settings(self, validated_data):
        default_attribute_mapping = SAMLProvider.default_attribute_mapping
        attribute_mapping = {
            "uid": validated_data.pop("attribute_mapping_uid", None),
            "email_verified": validated_data.pop(
                "attribute_mapping_email_verified", None
            ),
            "email": validated_data.pop("attribute_mapping_email", None),
        }
        return {
            "attribute_mapping": {
                key: value if value is not None else default_attribute_mapping[key]
                for key, value in attribute_mapping.items()
            },
            "idp": {
                "entity_id": validated_data.pop("idp_entity_id", ""),
                "metadata_url": validated_data.pop("metadata_url", ""),
                "sso_url": validated_data.pop("sso_url", ""),
                "slo_url": validated_data.pop("slo_url", ""),
                "x509cert": validated_data.pop("x509cert", ""),
            },
            "sp": {
                # Optional entity ID of the SP. If not set, defaults to the `saml_metadata` urlpattern
                "entity_id": validated_data.pop("sp_entity_id", ""),
            },
            # Advanced settings.
            "advanced": {
                "allow_repeat_attribute_name": validated_data.pop(
                    "allow_repeat_attribute_name", True
                ),
                "allow_single_label_domains": validated_data.pop(
                    "allow_single_label_domains", False
                ),
                "authn_request_signed": validated_data.pop(
                    "authn_request_signed", False
                ),
                "digest_algorithm": validated_data.pop(
                    "digest_algorithm",
                    "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
                ),
                "logout_request_signed": validated_data.pop(
                    "logout_request_signed", False
                ),
                "logout_response_signed": validated_data.pop(
                    "logout_response_signed", False
                ),
                "metadata_signed": validated_data.pop("metadata_signed", False),
                "name_id_encrypted": validated_data.pop("name_id_encrypted", False),
                "reject_deprecated_algorithm": validated_data.pop(
                    "reject_deprecated_algorithm", True
                ),
                # Due to security concerns, IdP initiated SSO is rejected by default.
                "reject_idp_initiated_sso": validated_data.pop(
                    "reject_idp_initiated_sso", False
                ),
                "signature_algorithm": validated_data.pop(
                    "signature_algorithm",
                    "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
                ),
                "want_assertion_encrypted": validated_data.pop(
                    "want_assertion_encrypted", False
                ),
                "want_assertion_signed": validated_data.pop(
                    "want_assertion_signed", False
                ),
                "want_attribute_statement": validated_data.pop(
                    "want_attribute_statement", True
                ),
                "want_message_signed": validated_data.pop("want_message_signed", False),
                "want_name_id": validated_data.pop("want_name_id", False),
                "want_name_id_encrypted": validated_data.pop(
                    "want_name_id_encrypted", False
                ),
            },
        }
