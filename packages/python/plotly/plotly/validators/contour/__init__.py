import sys

if sys.version_info < (3, 7):
    from ._zsrc import ZsrcValidator
    from ._zmin import ZminValidator
    from ._zmid import ZmidValidator
    from ._zmax import ZmaxValidator
    from ._zhoverformat import ZhoverformatValidator
    from ._zauto import ZautoValidator
    from ._z import ZValidator
    from ._ytype import YtypeValidator
    from ._ysrc import YsrcValidator
    from ._ycalendar import YcalendarValidator
    from ._yaxis import YaxisValidator
    from ._y0 import Y0Validator
    from ._y import YValidator
    from ._xtype import XtypeValidator
    from ._xsrc import XsrcValidator
    from ._xcalendar import XcalendarValidator
    from ._xaxis import XaxisValidator
    from ._x0 import X0Validator
    from ._x import XValidator
    from ._visible import VisibleValidator
    from ._uirevision import UirevisionValidator
    from ._uid import UidValidator
    from ._transpose import TransposeValidator
    from ._textsrc import TextsrcValidator
    from ._text import TextValidator
    from ._stream import StreamValidator
    from ._showscale import ShowscaleValidator
    from ._showlegend import ShowlegendValidator
    from ._reversescale import ReversescaleValidator
    from ._opacity import OpacityValidator
    from ._ncontours import NcontoursValidator
    from ._name import NameValidator
    from ._metasrc import MetasrcValidator
    from ._meta import MetaValidator
    from ._line import LineValidator
    from ._legendgroup import LegendgroupValidator
    from ._idssrc import IdssrcValidator
    from ._ids import IdsValidator
    from ._hovertextsrc import HovertextsrcValidator
    from ._hovertext import HovertextValidator
    from ._hovertemplatesrc import HovertemplatesrcValidator
    from ._hovertemplate import HovertemplateValidator
    from ._hoverongaps import HoverongapsValidator
    from ._hoverlabel import HoverlabelValidator
    from ._hoverinfosrc import HoverinfosrcValidator
    from ._hoverinfo import HoverinfoValidator
    from ._fillcolor import FillcolorValidator
    from ._dy import DyValidator
    from ._dx import DxValidator
    from ._customdatasrc import CustomdatasrcValidator
    from ._customdata import CustomdataValidator
    from ._contours import ContoursValidator
    from ._connectgaps import ConnectgapsValidator
    from ._colorscale import ColorscaleValidator
    from ._colorbar import ColorbarValidator
    from ._coloraxis import ColoraxisValidator
    from ._autocontour import AutocontourValidator
    from ._autocolorscale import AutocolorscaleValidator
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [],
        [
            "._zsrc.ZsrcValidator",
            "._zmin.ZminValidator",
            "._zmid.ZmidValidator",
            "._zmax.ZmaxValidator",
            "._zhoverformat.ZhoverformatValidator",
            "._zauto.ZautoValidator",
            "._z.ZValidator",
            "._ytype.YtypeValidator",
            "._ysrc.YsrcValidator",
            "._ycalendar.YcalendarValidator",
            "._yaxis.YaxisValidator",
            "._y0.Y0Validator",
            "._y.YValidator",
            "._xtype.XtypeValidator",
            "._xsrc.XsrcValidator",
            "._xcalendar.XcalendarValidator",
            "._xaxis.XaxisValidator",
            "._x0.X0Validator",
            "._x.XValidator",
            "._visible.VisibleValidator",
            "._uirevision.UirevisionValidator",
            "._uid.UidValidator",
            "._transpose.TransposeValidator",
            "._textsrc.TextsrcValidator",
            "._text.TextValidator",
            "._stream.StreamValidator",
            "._showscale.ShowscaleValidator",
            "._showlegend.ShowlegendValidator",
            "._reversescale.ReversescaleValidator",
            "._opacity.OpacityValidator",
            "._ncontours.NcontoursValidator",
            "._name.NameValidator",
            "._metasrc.MetasrcValidator",
            "._meta.MetaValidator",
            "._line.LineValidator",
            "._legendgroup.LegendgroupValidator",
            "._idssrc.IdssrcValidator",
            "._ids.IdsValidator",
            "._hovertextsrc.HovertextsrcValidator",
            "._hovertext.HovertextValidator",
            "._hovertemplatesrc.HovertemplatesrcValidator",
            "._hovertemplate.HovertemplateValidator",
            "._hoverongaps.HoverongapsValidator",
            "._hoverlabel.HoverlabelValidator",
            "._hoverinfosrc.HoverinfosrcValidator",
            "._hoverinfo.HoverinfoValidator",
            "._fillcolor.FillcolorValidator",
            "._dy.DyValidator",
            "._dx.DxValidator",
            "._customdatasrc.CustomdatasrcValidator",
            "._customdata.CustomdataValidator",
            "._contours.ContoursValidator",
            "._connectgaps.ConnectgapsValidator",
            "._colorscale.ColorscaleValidator",
            "._colorbar.ColorbarValidator",
            "._coloraxis.ColoraxisValidator",
            "._autocontour.AutocontourValidator",
            "._autocolorscale.AutocolorscaleValidator",
        ],
    )
