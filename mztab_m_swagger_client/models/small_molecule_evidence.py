# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class SmallMoleculeEvidence(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'prefix': 'str',
        'header_prefix': 'str',
        'sme_id': 'int',
        'evidence_input_id': 'str',
        'database_identifier': 'str',
        'chemical_formula': 'str',
        'smiles': 'str',
        'inchi': 'str',
        'chemical_name': 'str',
        'uri': 'str',
        'derivatized_form': 'Parameter',
        'adduct_ion': 'str',
        'exp_mass_to_charge': 'float',
        'charge': 'int',
        'theoretical_mass_to_charge': 'float',
        'spectra_ref': 'list[SpectraRef]',
        'identification_method': 'Parameter',
        'ms_level': 'Parameter',
        'id_confidence_measure': 'list[float]',
        'rank': 'int',
        'opt': 'list[OptColumnMapping]',
        'comment': 'list[Comment]'
    }

    attribute_map = {
        'prefix': 'prefix',
        'header_prefix': 'header_prefix',
        'sme_id': 'sme_id',
        'evidence_input_id': 'evidence_input_id',
        'database_identifier': 'database_identifier',
        'chemical_formula': 'chemical_formula',
        'smiles': 'smiles',
        'inchi': 'inchi',
        'chemical_name': 'chemical_name',
        'uri': 'uri',
        'derivatized_form': 'derivatized_form',
        'adduct_ion': 'adduct_ion',
        'exp_mass_to_charge': 'exp_mass_to_charge',
        'charge': 'charge',
        'theoretical_mass_to_charge': 'theoretical_mass_to_charge',
        'spectra_ref': 'spectra_ref',
        'identification_method': 'identification_method',
        'ms_level': 'ms_level',
        'id_confidence_measure': 'id_confidence_measure',
        'rank': 'rank',
        'opt': 'opt',
        'comment': 'comment'
    }

    def __init__(self, prefix='SME', header_prefix='SEH', sme_id=None, evidence_input_id=None, database_identifier=None, chemical_formula=None, smiles=None, inchi=None, chemical_name=None, uri=None, derivatized_form=None, adduct_ion=None, exp_mass_to_charge=None, charge=None, theoretical_mass_to_charge=None, spectra_ref=None, identification_method=None, ms_level=None, id_confidence_measure=None, rank=1, opt=None, comment=None, local_vars_configuration=None):  # noqa: E501
        """SmallMoleculeEvidence - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._prefix = None
        self._header_prefix = None
        self._sme_id = None
        self._evidence_input_id = None
        self._database_identifier = None
        self._chemical_formula = None
        self._smiles = None
        self._inchi = None
        self._chemical_name = None
        self._uri = None
        self._derivatized_form = None
        self._adduct_ion = None
        self._exp_mass_to_charge = None
        self._charge = None
        self._theoretical_mass_to_charge = None
        self._spectra_ref = None
        self._identification_method = None
        self._ms_level = None
        self._id_confidence_measure = None
        self._rank = None
        self._opt = None
        self._comment = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if header_prefix is not None:
            self.header_prefix = header_prefix
        self.sme_id = sme_id
        self.evidence_input_id = evidence_input_id
        self.database_identifier = database_identifier
        if chemical_formula is not None:
            self.chemical_formula = chemical_formula
        if smiles is not None:
            self.smiles = smiles
        if inchi is not None:
            self.inchi = inchi
        if chemical_name is not None:
            self.chemical_name = chemical_name
        if uri is not None:
            self.uri = uri
        if derivatized_form is not None:
            self.derivatized_form = derivatized_form
        if adduct_ion is not None:
            self.adduct_ion = adduct_ion
        self.exp_mass_to_charge = exp_mass_to_charge
        self.charge = charge
        self.theoretical_mass_to_charge = theoretical_mass_to_charge
        self.spectra_ref = spectra_ref
        self.identification_method = identification_method
        self.ms_level = ms_level
        if id_confidence_measure is not None:
            self.id_confidence_measure = id_confidence_measure
        self.rank = rank
        if opt is not None:
            self.opt = opt
        if comment is not None:
            self.comment = comment

    @property
    def prefix(self):
        """Gets the prefix of this SmallMoleculeEvidence.  # noqa: E501

        The small molecule evidence table row prefix. SME MUST be used for rows of the small molecule evidence table.  # noqa: E501

        :return: The prefix of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this SmallMoleculeEvidence.

        The small molecule evidence table row prefix. SME MUST be used for rows of the small molecule evidence table.  # noqa: E501

        :param prefix: The prefix of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """
        allowed_values = ["SME"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and prefix not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `prefix` ({0}), must be one of {1}"  # noqa: E501
                .format(prefix, allowed_values)
            )

        self._prefix = prefix

    @property
    def header_prefix(self):
        """Gets the header_prefix of this SmallMoleculeEvidence.  # noqa: E501

        The small molecule evidence table header prefix. SEH MUST be used for the small molecule evidence table header line (the column labels).  # noqa: E501

        :return: The header_prefix of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._header_prefix

    @header_prefix.setter
    def header_prefix(self, header_prefix):
        """Sets the header_prefix of this SmallMoleculeEvidence.

        The small molecule evidence table header prefix. SEH MUST be used for the small molecule evidence table header line (the column labels).  # noqa: E501

        :param header_prefix: The header_prefix of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """
        allowed_values = ["SEH"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and header_prefix not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `header_prefix` ({0}), must be one of {1}"  # noqa: E501
                .format(header_prefix, allowed_values)
            )

        self._header_prefix = header_prefix

    @property
    def sme_id(self):
        """Gets the sme_id of this SmallMoleculeEvidence.  # noqa: E501

        A within file unique identifier for the small molecule evidence result.  # noqa: E501

        :return: The sme_id of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: int
        """
        return self._sme_id

    @sme_id.setter
    def sme_id(self, sme_id):
        """Sets the sme_id of this SmallMoleculeEvidence.

        A within file unique identifier for the small molecule evidence result.  # noqa: E501

        :param sme_id: The sme_id of this SmallMoleculeEvidence.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sme_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sme_id`, must not be `None`")  # noqa: E501

        self._sme_id = sme_id

    @property
    def evidence_input_id(self):
        """Gets the evidence_input_id of this SmallMoleculeEvidence.  # noqa: E501

        A within file unique identifier for the input data used to support this identification e.g. fragment spectrum, RT and m/z pair, isotope profile that was used for the identification process, to serve as a grouping mechanism, whereby multiple rows of results from the same input data share the same ID. The identifiers may be human readable but should not be assumed to be interpretable. For example, if fragmentation spectra have been searched then the ID may be the spectrum reference, or for accurate mass search, the ms_run[2]:458.75.  # noqa: E501

        :return: The evidence_input_id of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._evidence_input_id

    @evidence_input_id.setter
    def evidence_input_id(self, evidence_input_id):
        """Sets the evidence_input_id of this SmallMoleculeEvidence.

        A within file unique identifier for the input data used to support this identification e.g. fragment spectrum, RT and m/z pair, isotope profile that was used for the identification process, to serve as a grouping mechanism, whereby multiple rows of results from the same input data share the same ID. The identifiers may be human readable but should not be assumed to be interpretable. For example, if fragmentation spectra have been searched then the ID may be the spectrum reference, or for accurate mass search, the ms_run[2]:458.75.  # noqa: E501

        :param evidence_input_id: The evidence_input_id of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and evidence_input_id is None:  # noqa: E501
            raise ValueError("Invalid value for `evidence_input_id`, must not be `None`")  # noqa: E501

        self._evidence_input_id = evidence_input_id

    @property
    def database_identifier(self):
        """Gets the database_identifier of this SmallMoleculeEvidence.  # noqa: E501

        The putative identification for the small molecule sourced from an external database, using the same prefix specified in database[1-n]-prefix.  This could include additionally a chemical class or an identifier to a spectral library entity, even if its actual identity is unknown.  For the “no database” case, \"null\" must be used. The unprefixed use of \"null\" is prohibited for any other case. If no putative identification can be reported for a particular database, it MUST be reported as the database prefix followed by null.   # noqa: E501

        :return: The database_identifier of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._database_identifier

    @database_identifier.setter
    def database_identifier(self, database_identifier):
        """Sets the database_identifier of this SmallMoleculeEvidence.

        The putative identification for the small molecule sourced from an external database, using the same prefix specified in database[1-n]-prefix.  This could include additionally a chemical class or an identifier to a spectral library entity, even if its actual identity is unknown.  For the “no database” case, \"null\" must be used. The unprefixed use of \"null\" is prohibited for any other case. If no putative identification can be reported for a particular database, it MUST be reported as the database prefix followed by null.   # noqa: E501

        :param database_identifier: The database_identifier of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and database_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `database_identifier`, must not be `None`")  # noqa: E501

        self._database_identifier = database_identifier

    @property
    def chemical_formula(self):
        """Gets the chemical_formula of this SmallMoleculeEvidence.  # noqa: E501

        The chemical formula of the identified compound e.g. in a database, assumed to match the theoretical mass to charge (in some cases this will be the derivatized form, including adducts and protons).  This should be specified in Hill notation (EA Hill 1900), i.e. elements in the order C, H and then alphabetically all other elements. Counts of one may be omitted. Elements should be capitalized properly to avoid confusion (e.g., “CO” vs. “Co”). The chemical formula reported should refer to the neutral form. Charge state is reported by the charge field.  Example N-acetylglucosamine would be encoded by the string “C8H15NO6”   # noqa: E501

        :return: The chemical_formula of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._chemical_formula

    @chemical_formula.setter
    def chemical_formula(self, chemical_formula):
        """Sets the chemical_formula of this SmallMoleculeEvidence.

        The chemical formula of the identified compound e.g. in a database, assumed to match the theoretical mass to charge (in some cases this will be the derivatized form, including adducts and protons).  This should be specified in Hill notation (EA Hill 1900), i.e. elements in the order C, H and then alphabetically all other elements. Counts of one may be omitted. Elements should be capitalized properly to avoid confusion (e.g., “CO” vs. “Co”). The chemical formula reported should refer to the neutral form. Charge state is reported by the charge field.  Example N-acetylglucosamine would be encoded by the string “C8H15NO6”   # noqa: E501

        :param chemical_formula: The chemical_formula of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """

        self._chemical_formula = chemical_formula

    @property
    def smiles(self):
        """Gets the smiles of this SmallMoleculeEvidence.  # noqa: E501

        The potential molecule’s structure in the simplified molecular-input line-entry system (SMILES) for the small molecule.  # noqa: E501

        :return: The smiles of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this SmallMoleculeEvidence.

        The potential molecule’s structure in the simplified molecular-input line-entry system (SMILES) for the small molecule.  # noqa: E501

        :param smiles: The smiles of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """

        self._smiles = smiles

    @property
    def inchi(self):
        """Gets the inchi of this SmallMoleculeEvidence.  # noqa: E501

        A standard IUPAC International Chemical Identifier (InChI) for the given substance.  # noqa: E501

        :return: The inchi of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._inchi

    @inchi.setter
    def inchi(self, inchi):
        """Sets the inchi of this SmallMoleculeEvidence.

        A standard IUPAC International Chemical Identifier (InChI) for the given substance.  # noqa: E501

        :param inchi: The inchi of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """

        self._inchi = inchi

    @property
    def chemical_name(self):
        """Gets the chemical_name of this SmallMoleculeEvidence.  # noqa: E501

        The small molecule’s chemical/common name, or general description if a chemical name is unavailable.  # noqa: E501

        :return: The chemical_name of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._chemical_name

    @chemical_name.setter
    def chemical_name(self, chemical_name):
        """Sets the chemical_name of this SmallMoleculeEvidence.

        The small molecule’s chemical/common name, or general description if a chemical name is unavailable.  # noqa: E501

        :param chemical_name: The chemical_name of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """

        self._chemical_name = chemical_name

    @property
    def uri(self):
        """Gets the uri of this SmallMoleculeEvidence.  # noqa: E501

        A URI pointing to the small molecule’s entry in a database (e.g., the small molecule’s HMDB, Chebi or KEGG entry).  # noqa: E501

        :return: The uri of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this SmallMoleculeEvidence.

        A URI pointing to the small molecule’s entry in a database (e.g., the small molecule’s HMDB, Chebi or KEGG entry).  # noqa: E501

        :param uri: The uri of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def derivatized_form(self):
        """Gets the derivatized_form of this SmallMoleculeEvidence.  # noqa: E501


        :return: The derivatized_form of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: Parameter
        """
        return self._derivatized_form

    @derivatized_form.setter
    def derivatized_form(self, derivatized_form):
        """Sets the derivatized_form of this SmallMoleculeEvidence.


        :param derivatized_form: The derivatized_form of this SmallMoleculeEvidence.  # noqa: E501
        :type: Parameter
        """

        self._derivatized_form = derivatized_form

    @property
    def adduct_ion(self):
        """Gets the adduct_ion of this SmallMoleculeEvidence.  # noqa: E501

        The assumed classification of this molecule’s adduct ion after detection, following the general style in the 2013 IUPAC recommendations on terms relating to MS e.g. [M+H]+, [M+Na]1+, [M+NH4]1+, [M-H]1-, [M+Cl]1-. If the adduct classification is ambiguous with regards to identification evidence it MAY be null.  # noqa: E501

        :return: The adduct_ion of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._adduct_ion

    @adduct_ion.setter
    def adduct_ion(self, adduct_ion):
        """Sets the adduct_ion of this SmallMoleculeEvidence.

        The assumed classification of this molecule’s adduct ion after detection, following the general style in the 2013 IUPAC recommendations on terms relating to MS e.g. [M+H]+, [M+Na]1+, [M+NH4]1+, [M-H]1-, [M+Cl]1-. If the adduct classification is ambiguous with regards to identification evidence it MAY be null.  # noqa: E501

        :param adduct_ion: The adduct_ion of this SmallMoleculeEvidence.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                adduct_ion is not None and not re.search(r'^\[\d*M([-][\w]*)\]\d*[+-]$', adduct_ion)):  # noqa: E501
            raise ValueError(r"Invalid value for `adduct_ion`, must be a follow pattern or equal to `/^\[\d*M([-][\w]*)\]\d*[+-]$/`")  # noqa: E501

        self._adduct_ion = adduct_ion

    @property
    def exp_mass_to_charge(self):
        """Gets the exp_mass_to_charge of this SmallMoleculeEvidence.  # noqa: E501

        The experimental mass/charge value for the precursor ion. If multiple adduct forms have been combined into a single identification event/search, then a single value e.g. for the protonated form SHOULD be reported here.  # noqa: E501

        :return: The exp_mass_to_charge of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: float
        """
        return self._exp_mass_to_charge

    @exp_mass_to_charge.setter
    def exp_mass_to_charge(self, exp_mass_to_charge):
        """Sets the exp_mass_to_charge of this SmallMoleculeEvidence.

        The experimental mass/charge value for the precursor ion. If multiple adduct forms have been combined into a single identification event/search, then a single value e.g. for the protonated form SHOULD be reported here.  # noqa: E501

        :param exp_mass_to_charge: The exp_mass_to_charge of this SmallMoleculeEvidence.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and exp_mass_to_charge is None:  # noqa: E501
            raise ValueError("Invalid value for `exp_mass_to_charge`, must not be `None`")  # noqa: E501

        self._exp_mass_to_charge = exp_mass_to_charge

    @property
    def charge(self):
        """Gets the charge of this SmallMoleculeEvidence.  # noqa: E501

        The small molecule evidence’s charge value using positive integers both for positive and negative polarity modes.  # noqa: E501

        :return: The charge of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: int
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this SmallMoleculeEvidence.

        The small molecule evidence’s charge value using positive integers both for positive and negative polarity modes.  # noqa: E501

        :param charge: The charge of this SmallMoleculeEvidence.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and charge is None:  # noqa: E501
            raise ValueError("Invalid value for `charge`, must not be `None`")  # noqa: E501

        self._charge = charge

    @property
    def theoretical_mass_to_charge(self):
        """Gets the theoretical_mass_to_charge of this SmallMoleculeEvidence.  # noqa: E501

        The theoretical mass/charge value for the small molecule or the database mass/charge value (for a spectral library match).  # noqa: E501

        :return: The theoretical_mass_to_charge of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: float
        """
        return self._theoretical_mass_to_charge

    @theoretical_mass_to_charge.setter
    def theoretical_mass_to_charge(self, theoretical_mass_to_charge):
        """Sets the theoretical_mass_to_charge of this SmallMoleculeEvidence.

        The theoretical mass/charge value for the small molecule or the database mass/charge value (for a spectral library match).  # noqa: E501

        :param theoretical_mass_to_charge: The theoretical_mass_to_charge of this SmallMoleculeEvidence.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and theoretical_mass_to_charge is None:  # noqa: E501
            raise ValueError("Invalid value for `theoretical_mass_to_charge`, must not be `None`")  # noqa: E501

        self._theoretical_mass_to_charge = theoretical_mass_to_charge

    @property
    def spectra_ref(self):
        """Gets the spectra_ref of this SmallMoleculeEvidence.  # noqa: E501

        Reference to a spectrum in a spectrum file, for example a fragmentation spectrum has been used to support the identification. If a separate spectrum file has been used for fragmentation spectrum, this MUST be reported in the metadata section as additional ms_runs. The reference must be in the format ms_run[1-n]:{SPECTRA_REF} where SPECTRA_REF MUST follow the format defined in 5.2 (including references to chromatograms where these are used to inform identification). Multiple spectra MUST be referenced using a “|” delimited list for the (rare) cases in which search engines have combined or aggregated multiple spectra in advance of the search to make identifications.  If a fragmentation spectrum has not been used, the value should indicate the ms_run to which is identification is mapped e.g. “ms_run[1]”.   # noqa: E501

        :return: The spectra_ref of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: list[SpectraRef]
        """
        return self._spectra_ref

    @spectra_ref.setter
    def spectra_ref(self, spectra_ref):
        """Sets the spectra_ref of this SmallMoleculeEvidence.

        Reference to a spectrum in a spectrum file, for example a fragmentation spectrum has been used to support the identification. If a separate spectrum file has been used for fragmentation spectrum, this MUST be reported in the metadata section as additional ms_runs. The reference must be in the format ms_run[1-n]:{SPECTRA_REF} where SPECTRA_REF MUST follow the format defined in 5.2 (including references to chromatograms where these are used to inform identification). Multiple spectra MUST be referenced using a “|” delimited list for the (rare) cases in which search engines have combined or aggregated multiple spectra in advance of the search to make identifications.  If a fragmentation spectrum has not been used, the value should indicate the ms_run to which is identification is mapped e.g. “ms_run[1]”.   # noqa: E501

        :param spectra_ref: The spectra_ref of this SmallMoleculeEvidence.  # noqa: E501
        :type: list[SpectraRef]
        """
        if self.local_vars_configuration.client_side_validation and spectra_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `spectra_ref`, must not be `None`")  # noqa: E501

        self._spectra_ref = spectra_ref

    @property
    def identification_method(self):
        """Gets the identification_method of this SmallMoleculeEvidence.  # noqa: E501


        :return: The identification_method of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: Parameter
        """
        return self._identification_method

    @identification_method.setter
    def identification_method(self, identification_method):
        """Sets the identification_method of this SmallMoleculeEvidence.


        :param identification_method: The identification_method of this SmallMoleculeEvidence.  # noqa: E501
        :type: Parameter
        """
        if self.local_vars_configuration.client_side_validation and identification_method is None:  # noqa: E501
            raise ValueError("Invalid value for `identification_method`, must not be `None`")  # noqa: E501

        self._identification_method = identification_method

    @property
    def ms_level(self):
        """Gets the ms_level of this SmallMoleculeEvidence.  # noqa: E501


        :return: The ms_level of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: Parameter
        """
        return self._ms_level

    @ms_level.setter
    def ms_level(self, ms_level):
        """Sets the ms_level of this SmallMoleculeEvidence.


        :param ms_level: The ms_level of this SmallMoleculeEvidence.  # noqa: E501
        :type: Parameter
        """
        if self.local_vars_configuration.client_side_validation and ms_level is None:  # noqa: E501
            raise ValueError("Invalid value for `ms_level`, must not be `None`")  # noqa: E501

        self._ms_level = ms_level

    @property
    def id_confidence_measure(self):
        """Gets the id_confidence_measure of this SmallMoleculeEvidence.  # noqa: E501

        Any statistical value or score for the identification. The metadata section reports the type of score used, as id_confidence_measure[1-n] of type Param.  # noqa: E501

        :return: The id_confidence_measure of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: list[float]
        """
        return self._id_confidence_measure

    @id_confidence_measure.setter
    def id_confidence_measure(self, id_confidence_measure):
        """Sets the id_confidence_measure of this SmallMoleculeEvidence.

        Any statistical value or score for the identification. The metadata section reports the type of score used, as id_confidence_measure[1-n] of type Param.  # noqa: E501

        :param id_confidence_measure: The id_confidence_measure of this SmallMoleculeEvidence.  # noqa: E501
        :type: list[float]
        """

        self._id_confidence_measure = id_confidence_measure

    @property
    def rank(self):
        """Gets the rank of this SmallMoleculeEvidence.  # noqa: E501

        The rank of this identification from this approach as increasing integers from 1 (best ranked identification). Ties (equal score) are represented by using the same rank – defaults to 1 if there is no ranking system used.  # noqa: E501

        :return: The rank of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this SmallMoleculeEvidence.

        The rank of this identification from this approach as increasing integers from 1 (best ranked identification). Ties (equal score) are represented by using the same rank – defaults to 1 if there is no ranking system used.  # noqa: E501

        :param rank: The rank of this SmallMoleculeEvidence.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and rank is None:  # noqa: E501
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rank is not None and rank < 1):  # noqa: E501
            raise ValueError("Invalid value for `rank`, must be a value greater than or equal to `1`")  # noqa: E501

        self._rank = rank

    @property
    def opt(self):
        """Gets the opt of this SmallMoleculeEvidence.  # noqa: E501

        Additional columns can be added to the end of the small molecule evidence table. These column headers MUST start with the prefix “opt_” followed by the {identifier} of the object they reference: assay, study variable, MS run or “global” (if the value relates to all replicates). Column names MUST only contain the following characters: ‘A’-‘Z’, ‘a’-‘z’, ‘0’-‘9’, ‘’, ‘-’, ‘[’, ‘]’, and ‘:’. CV parameter accessions MAY be used for optional columns following the format: opt{identifier}_cv_{accession}_\\{parameter name}. Spaces within the parameter’s name MUST be replaced by ‘_’.   # noqa: E501

        :return: The opt of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: list[OptColumnMapping]
        """
        return self._opt

    @opt.setter
    def opt(self, opt):
        """Sets the opt of this SmallMoleculeEvidence.

        Additional columns can be added to the end of the small molecule evidence table. These column headers MUST start with the prefix “opt_” followed by the {identifier} of the object they reference: assay, study variable, MS run or “global” (if the value relates to all replicates). Column names MUST only contain the following characters: ‘A’-‘Z’, ‘a’-‘z’, ‘0’-‘9’, ‘’, ‘-’, ‘[’, ‘]’, and ‘:’. CV parameter accessions MAY be used for optional columns following the format: opt{identifier}_cv_{accession}_\\{parameter name}. Spaces within the parameter’s name MUST be replaced by ‘_’.   # noqa: E501

        :param opt: The opt of this SmallMoleculeEvidence.  # noqa: E501
        :type: list[OptColumnMapping]
        """

        self._opt = opt

    @property
    def comment(self):
        """Gets the comment of this SmallMoleculeEvidence.  # noqa: E501


        :return: The comment of this SmallMoleculeEvidence.  # noqa: E501
        :rtype: list[Comment]
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SmallMoleculeEvidence.


        :param comment: The comment of this SmallMoleculeEvidence.  # noqa: E501
        :type: list[Comment]
        """

        self._comment = comment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmallMoleculeEvidence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmallMoleculeEvidence):
            return True

        return self.to_dict() != other.to_dict()
