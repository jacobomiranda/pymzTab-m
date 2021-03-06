# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mztab_m_swagger_client.models.comment import Comment  # noqa: F401,E501
from mztab_m_swagger_client.models.opt_column_mapping import OptColumnMapping  # noqa: F401,E501
from mztab_m_swagger_client.models.parameter import Parameter  # noqa: F401,E501


class SmallMoleculeFeature(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'prefix': 'str',
        'header_prefix': 'str',
        'smf_id': 'int',
        'sme_id_refs': 'list[int]',
        'sme_id_ref_ambiguity_code': 'int',
        'adduct_ion': 'str',
        'isotopomer': 'Parameter',
        'exp_mass_to_charge': 'float',
        'charge': 'int',
        'retention_time_in_seconds': 'float',
        'retention_time_in_seconds_start': 'float',
        'retention_time_in_seconds_end': 'float',
        'abundance_assay': 'list[float]',
        'opt': 'list[OptColumnMapping]',
        'comment': 'list[Comment]'
    }

    attribute_map = {
        'prefix': 'prefix',
        'header_prefix': 'header_prefix',
        'smf_id': 'smf_id',
        'sme_id_refs': 'sme_id_refs',
        'sme_id_ref_ambiguity_code': 'sme_id_ref_ambiguity_code',
        'adduct_ion': 'adduct_ion',
        'isotopomer': 'isotopomer',
        'exp_mass_to_charge': 'exp_mass_to_charge',
        'charge': 'charge',
        'retention_time_in_seconds': 'retention_time_in_seconds',
        'retention_time_in_seconds_start': 'retention_time_in_seconds_start',
        'retention_time_in_seconds_end': 'retention_time_in_seconds_end',
        'abundance_assay': 'abundance_assay',
        'opt': 'opt',
        'comment': 'comment'
    }

    def __init__(self, prefix='SMF', header_prefix='SFH', smf_id=None, sme_id_refs=None, sme_id_ref_ambiguity_code=None, adduct_ion=None, isotopomer=None, exp_mass_to_charge=None, charge=None, retention_time_in_seconds=None, retention_time_in_seconds_start=None, retention_time_in_seconds_end=None, abundance_assay=None, opt=None, comment=None):  # noqa: E501
        """SmallMoleculeFeature - a model defined in Swagger"""  # noqa: E501

        self._prefix = None
        self._header_prefix = None
        self._smf_id = None
        self._sme_id_refs = None
        self._sme_id_ref_ambiguity_code = None
        self._adduct_ion = None
        self._isotopomer = None
        self._exp_mass_to_charge = None
        self._charge = None
        self._retention_time_in_seconds = None
        self._retention_time_in_seconds_start = None
        self._retention_time_in_seconds_end = None
        self._abundance_assay = None
        self._opt = None
        self._comment = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if header_prefix is not None:
            self.header_prefix = header_prefix
        self.smf_id = smf_id
        if sme_id_refs is not None:
            self.sme_id_refs = sme_id_refs
        if sme_id_ref_ambiguity_code is not None:
            self.sme_id_ref_ambiguity_code = sme_id_ref_ambiguity_code
        if adduct_ion is not None:
            self.adduct_ion = adduct_ion
        if isotopomer is not None:
            self.isotopomer = isotopomer
        self.exp_mass_to_charge = exp_mass_to_charge
        self.charge = charge
        if retention_time_in_seconds is not None:
            self.retention_time_in_seconds = retention_time_in_seconds
        if retention_time_in_seconds_start is not None:
            self.retention_time_in_seconds_start = retention_time_in_seconds_start
        if retention_time_in_seconds_end is not None:
            self.retention_time_in_seconds_end = retention_time_in_seconds_end
        if abundance_assay is not None:
            self.abundance_assay = abundance_assay
        if opt is not None:
            self.opt = opt
        if comment is not None:
            self.comment = comment

    @property
    def prefix(self):
        """Gets the prefix of this SmallMoleculeFeature.  # noqa: E501

        The small molecule feature table row prefix. SMF MUST be used for rows of the small molecule feature table.  # noqa: E501

        :return: The prefix of this SmallMoleculeFeature.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this SmallMoleculeFeature.

        The small molecule feature table row prefix. SMF MUST be used for rows of the small molecule feature table.  # noqa: E501

        :param prefix: The prefix of this SmallMoleculeFeature.  # noqa: E501
        :type: str
        """
        allowed_values = ["SMF"]  # noqa: E501
        if prefix not in allowed_values:
            raise ValueError(
                "Invalid value for `prefix` ({0}), must be one of {1}"  # noqa: E501
                .format(prefix, allowed_values)
            )

        self._prefix = prefix

    @property
    def header_prefix(self):
        """Gets the header_prefix of this SmallMoleculeFeature.  # noqa: E501

        The small molecule feature table header prefix. SFH MUST be used for the small molecule feature table header line (the column labels).  # noqa: E501

        :return: The header_prefix of this SmallMoleculeFeature.  # noqa: E501
        :rtype: str
        """
        return self._header_prefix

    @header_prefix.setter
    def header_prefix(self, header_prefix):
        """Sets the header_prefix of this SmallMoleculeFeature.

        The small molecule feature table header prefix. SFH MUST be used for the small molecule feature table header line (the column labels).  # noqa: E501

        :param header_prefix: The header_prefix of this SmallMoleculeFeature.  # noqa: E501
        :type: str
        """
        allowed_values = ["SFH"]  # noqa: E501
        if header_prefix not in allowed_values:
            raise ValueError(
                "Invalid value for `header_prefix` ({0}), must be one of {1}"  # noqa: E501
                .format(header_prefix, allowed_values)
            )

        self._header_prefix = header_prefix

    @property
    def smf_id(self):
        """Gets the smf_id of this SmallMoleculeFeature.  # noqa: E501

        A within file unique identifier for the small molecule feature.  # noqa: E501

        :return: The smf_id of this SmallMoleculeFeature.  # noqa: E501
        :rtype: int
        """
        return self._smf_id

    @smf_id.setter
    def smf_id(self, smf_id):
        """Sets the smf_id of this SmallMoleculeFeature.

        A within file unique identifier for the small molecule feature.  # noqa: E501

        :param smf_id: The smf_id of this SmallMoleculeFeature.  # noqa: E501
        :type: int
        """
        if smf_id is None:
            raise ValueError("Invalid value for `smf_id`, must not be `None`")  # noqa: E501

        self._smf_id = smf_id

    @property
    def sme_id_refs(self):
        """Gets the sme_id_refs of this SmallMoleculeFeature.  # noqa: E501

        References to the identification evidence (SME elements) via referencing SME_ID values. Multiple values MAY be provided as a “|” separated list to indicate ambiguity in the identification or to indicate that different types of data supported the identifiction (see SME_ID_REF_ambiguity_code). For the case of a consensus approach where multiple adduct forms are used to infer the SML ID, different features should just reference the same SME_ID value(s).  # noqa: E501

        :return: The sme_id_refs of this SmallMoleculeFeature.  # noqa: E501
        :rtype: list[int]
        """
        return self._sme_id_refs

    @sme_id_refs.setter
    def sme_id_refs(self, sme_id_refs):
        """Sets the sme_id_refs of this SmallMoleculeFeature.

        References to the identification evidence (SME elements) via referencing SME_ID values. Multiple values MAY be provided as a “|” separated list to indicate ambiguity in the identification or to indicate that different types of data supported the identifiction (see SME_ID_REF_ambiguity_code). For the case of a consensus approach where multiple adduct forms are used to infer the SML ID, different features should just reference the same SME_ID value(s).  # noqa: E501

        :param sme_id_refs: The sme_id_refs of this SmallMoleculeFeature.  # noqa: E501
        :type: list[int]
        """

        self._sme_id_refs = sme_id_refs

    @property
    def sme_id_ref_ambiguity_code(self):
        """Gets the sme_id_ref_ambiguity_code of this SmallMoleculeFeature.  # noqa: E501

        If multiple values are given under SME_ID_REFS, one of the following codes MUST be provided. 1=Ambiguous identification; 2=Only different evidence streams for the same molecule with no ambiguity; 3=Both ambiguous identification and multiple evidence streams. If there are no or one value under SME_ID_REFs, this MUST be reported as null.  # noqa: E501

        :return: The sme_id_ref_ambiguity_code of this SmallMoleculeFeature.  # noqa: E501
        :rtype: int
        """
        return self._sme_id_ref_ambiguity_code

    @sme_id_ref_ambiguity_code.setter
    def sme_id_ref_ambiguity_code(self, sme_id_ref_ambiguity_code):
        """Sets the sme_id_ref_ambiguity_code of this SmallMoleculeFeature.

        If multiple values are given under SME_ID_REFS, one of the following codes MUST be provided. 1=Ambiguous identification; 2=Only different evidence streams for the same molecule with no ambiguity; 3=Both ambiguous identification and multiple evidence streams. If there are no or one value under SME_ID_REFs, this MUST be reported as null.  # noqa: E501

        :param sme_id_ref_ambiguity_code: The sme_id_ref_ambiguity_code of this SmallMoleculeFeature.  # noqa: E501
        :type: int
        """

        self._sme_id_ref_ambiguity_code = sme_id_ref_ambiguity_code

    @property
    def adduct_ion(self):
        """Gets the adduct_ion of this SmallMoleculeFeature.  # noqa: E501

        The assumed classification of this molecule’s adduct ion after detection, following the general style in the 2013 IUPAC recommendations on terms relating to MS e.g. [M+H]1+, [M+Na]1+, [M+NH4]1+, [M-H]1-, [M+Cl]1-, [M+H]1+.  # noqa: E501

        :return: The adduct_ion of this SmallMoleculeFeature.  # noqa: E501
        :rtype: str
        """
        return self._adduct_ion

    @adduct_ion.setter
    def adduct_ion(self, adduct_ion):
        """Sets the adduct_ion of this SmallMoleculeFeature.

        The assumed classification of this molecule’s adduct ion after detection, following the general style in the 2013 IUPAC recommendations on terms relating to MS e.g. [M+H]1+, [M+Na]1+, [M+NH4]1+, [M-H]1-, [M+Cl]1-, [M+H]1+.  # noqa: E501

        :param adduct_ion: The adduct_ion of this SmallMoleculeFeature.  # noqa: E501
        :type: str
        """
        if adduct_ion is not None and not re.search(r'^\[\d*M([+-][\w]*)\]\d*[+-]$', adduct_ion):  # noqa: E501
            raise ValueError(r"Invalid value for `adduct_ion`, must be a follow pattern or equal to `/^\\[\\d*M([+-][\\w]*)\\]\\d*[+-]$/`")  # noqa: E501

        self._adduct_ion = adduct_ion

    @property
    def isotopomer(self):
        """Gets the isotopomer of this SmallMoleculeFeature.  # noqa: E501

        If de-isotoping has not been performed, then the isotopomer quantified MUST be reported here e.g. “+1”, “+2”, “13C peak” using CV terms, otherwise (i.e. for approaches where SMF rows are de-isotoped features) this MUST be null.  # noqa: E501

        :return: The isotopomer of this SmallMoleculeFeature.  # noqa: E501
        :rtype: Parameter
        """
        return self._isotopomer

    @isotopomer.setter
    def isotopomer(self, isotopomer):
        """Sets the isotopomer of this SmallMoleculeFeature.

        If de-isotoping has not been performed, then the isotopomer quantified MUST be reported here e.g. “+1”, “+2”, “13C peak” using CV terms, otherwise (i.e. for approaches where SMF rows are de-isotoped features) this MUST be null.  # noqa: E501

        :param isotopomer: The isotopomer of this SmallMoleculeFeature.  # noqa: E501
        :type: Parameter
        """

        self._isotopomer = isotopomer

    @property
    def exp_mass_to_charge(self):
        """Gets the exp_mass_to_charge of this SmallMoleculeFeature.  # noqa: E501

        The experimental mass/charge value for the feature, by default assumed to be the mean across assays or a representative value. For approaches that report isotopomers as SMF rows, then the m/z of the isotopomer MUST be reported here.  # noqa: E501

        :return: The exp_mass_to_charge of this SmallMoleculeFeature.  # noqa: E501
        :rtype: float
        """
        return self._exp_mass_to_charge

    @exp_mass_to_charge.setter
    def exp_mass_to_charge(self, exp_mass_to_charge):
        """Sets the exp_mass_to_charge of this SmallMoleculeFeature.

        The experimental mass/charge value for the feature, by default assumed to be the mean across assays or a representative value. For approaches that report isotopomers as SMF rows, then the m/z of the isotopomer MUST be reported here.  # noqa: E501

        :param exp_mass_to_charge: The exp_mass_to_charge of this SmallMoleculeFeature.  # noqa: E501
        :type: float
        """
        if exp_mass_to_charge is None:
            raise ValueError("Invalid value for `exp_mass_to_charge`, must not be `None`")  # noqa: E501

        self._exp_mass_to_charge = exp_mass_to_charge

    @property
    def charge(self):
        """Gets the charge of this SmallMoleculeFeature.  # noqa: E501

        The feature’s charge value using positive integers both for positive and negative polarity modes.  # noqa: E501

        :return: The charge of this SmallMoleculeFeature.  # noqa: E501
        :rtype: int
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this SmallMoleculeFeature.

        The feature’s charge value using positive integers both for positive and negative polarity modes.  # noqa: E501

        :param charge: The charge of this SmallMoleculeFeature.  # noqa: E501
        :type: int
        """
        if charge is None:
            raise ValueError("Invalid value for `charge`, must not be `None`")  # noqa: E501

        self._charge = charge

    @property
    def retention_time_in_seconds(self):
        """Gets the retention_time_in_seconds of this SmallMoleculeFeature.  # noqa: E501

        The apex of the feature on the retention time axis, in a Master or aggregate MS run. Retention time MUST be reported in seconds. Retention time values for individual MS runs (i.e. before alignment) MAY be reported as optional columns. Retention time SHOULD only be null in the case of direct infusion MS or other techniques where a retention time value is absent or unknown. Relative retention time or retention time index values MAY be reported as optional columns, and could be considered for inclusion in future versions of mzTab as appropriate.  # noqa: E501

        :return: The retention_time_in_seconds of this SmallMoleculeFeature.  # noqa: E501
        :rtype: float
        """
        return self._retention_time_in_seconds

    @retention_time_in_seconds.setter
    def retention_time_in_seconds(self, retention_time_in_seconds):
        """Sets the retention_time_in_seconds of this SmallMoleculeFeature.

        The apex of the feature on the retention time axis, in a Master or aggregate MS run. Retention time MUST be reported in seconds. Retention time values for individual MS runs (i.e. before alignment) MAY be reported as optional columns. Retention time SHOULD only be null in the case of direct infusion MS or other techniques where a retention time value is absent or unknown. Relative retention time or retention time index values MAY be reported as optional columns, and could be considered for inclusion in future versions of mzTab as appropriate.  # noqa: E501

        :param retention_time_in_seconds: The retention_time_in_seconds of this SmallMoleculeFeature.  # noqa: E501
        :type: float
        """

        self._retention_time_in_seconds = retention_time_in_seconds

    @property
    def retention_time_in_seconds_start(self):
        """Gets the retention_time_in_seconds_start of this SmallMoleculeFeature.  # noqa: E501

        The start time of the feature on the retention time axis, in a Master or aggregate MS run. Retention time MUST be reported in seconds. Retention time start and end SHOULD only be null in the case of direct infusion MS or other techniques where a retention time value is absent or unknown and MAY be reported in optional columns.  # noqa: E501

        :return: The retention_time_in_seconds_start of this SmallMoleculeFeature.  # noqa: E501
        :rtype: float
        """
        return self._retention_time_in_seconds_start

    @retention_time_in_seconds_start.setter
    def retention_time_in_seconds_start(self, retention_time_in_seconds_start):
        """Sets the retention_time_in_seconds_start of this SmallMoleculeFeature.

        The start time of the feature on the retention time axis, in a Master or aggregate MS run. Retention time MUST be reported in seconds. Retention time start and end SHOULD only be null in the case of direct infusion MS or other techniques where a retention time value is absent or unknown and MAY be reported in optional columns.  # noqa: E501

        :param retention_time_in_seconds_start: The retention_time_in_seconds_start of this SmallMoleculeFeature.  # noqa: E501
        :type: float
        """

        self._retention_time_in_seconds_start = retention_time_in_seconds_start

    @property
    def retention_time_in_seconds_end(self):
        """Gets the retention_time_in_seconds_end of this SmallMoleculeFeature.  # noqa: E501

        The end time of the feature on the retention time axis, in a Master or aggregate MS run. Retention time MUST be reported in seconds. Retention time start and end SHOULD only be null in the case of direct infusion MS or other techniques where a retention time value is absent or unknown and MAY be reported in optional columns..  # noqa: E501

        :return: The retention_time_in_seconds_end of this SmallMoleculeFeature.  # noqa: E501
        :rtype: float
        """
        return self._retention_time_in_seconds_end

    @retention_time_in_seconds_end.setter
    def retention_time_in_seconds_end(self, retention_time_in_seconds_end):
        """Sets the retention_time_in_seconds_end of this SmallMoleculeFeature.

        The end time of the feature on the retention time axis, in a Master or aggregate MS run. Retention time MUST be reported in seconds. Retention time start and end SHOULD only be null in the case of direct infusion MS or other techniques where a retention time value is absent or unknown and MAY be reported in optional columns..  # noqa: E501

        :param retention_time_in_seconds_end: The retention_time_in_seconds_end of this SmallMoleculeFeature.  # noqa: E501
        :type: float
        """

        self._retention_time_in_seconds_end = retention_time_in_seconds_end

    @property
    def abundance_assay(self):
        """Gets the abundance_assay of this SmallMoleculeFeature.  # noqa: E501

        The feature’s abundance in every assay described in the metadata section MUST be reported. Null or zero values may be reported as appropriate.  # noqa: E501

        :return: The abundance_assay of this SmallMoleculeFeature.  # noqa: E501
        :rtype: list[float]
        """
        return self._abundance_assay

    @abundance_assay.setter
    def abundance_assay(self, abundance_assay):
        """Sets the abundance_assay of this SmallMoleculeFeature.

        The feature’s abundance in every assay described in the metadata section MUST be reported. Null or zero values may be reported as appropriate.  # noqa: E501

        :param abundance_assay: The abundance_assay of this SmallMoleculeFeature.  # noqa: E501
        :type: list[float]
        """

        self._abundance_assay = abundance_assay

    @property
    def opt(self):
        """Gets the opt of this SmallMoleculeFeature.  # noqa: E501

        Additional columns can be added to the end of the small molecule feature table. These column headers MUST start with the prefix “opt_” followed by the {identifier} of the object they reference: assay, study variable, MS run or “global” (if the value relates to all replicates). Column names MUST only contain the following characters: ‘A’-‘Z’, ‘a’-‘z’, ‘0’-‘9’, ‘’, ‘-’, ‘[’, ‘]’, and ‘:’. CV parameter accessions MAY be used for optional columns following the format: opt{identifier}_cv_{accession}_\\{parameter name}. Spaces within the parameter’s name MUST be replaced by ‘_’.   # noqa: E501

        :return: The opt of this SmallMoleculeFeature.  # noqa: E501
        :rtype: list[OptColumnMapping]
        """
        return self._opt

    @opt.setter
    def opt(self, opt):
        """Sets the opt of this SmallMoleculeFeature.

        Additional columns can be added to the end of the small molecule feature table. These column headers MUST start with the prefix “opt_” followed by the {identifier} of the object they reference: assay, study variable, MS run or “global” (if the value relates to all replicates). Column names MUST only contain the following characters: ‘A’-‘Z’, ‘a’-‘z’, ‘0’-‘9’, ‘’, ‘-’, ‘[’, ‘]’, and ‘:’. CV parameter accessions MAY be used for optional columns following the format: opt{identifier}_cv_{accession}_\\{parameter name}. Spaces within the parameter’s name MUST be replaced by ‘_’.   # noqa: E501

        :param opt: The opt of this SmallMoleculeFeature.  # noqa: E501
        :type: list[OptColumnMapping]
        """

        self._opt = opt

    @property
    def comment(self):
        """Gets the comment of this SmallMoleculeFeature.  # noqa: E501


        :return: The comment of this SmallMoleculeFeature.  # noqa: E501
        :rtype: list[Comment]
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SmallMoleculeFeature.


        :param comment: The comment of this SmallMoleculeFeature.  # noqa: E501
        :type: list[Comment]
        """

        self._comment = comment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SmallMoleculeFeature, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmallMoleculeFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
