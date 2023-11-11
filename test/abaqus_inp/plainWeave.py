from TexGen.Core import *


weave = CTextileWeave2D(2, 2, 1, 0.2, bool(1), bool(1))
weave.SetGapSize(0)
weave.SetYarnWidths(0.6)
weave.SwapPosition(0, 0)
weave.SwapPosition(1, 1)
weave.SetXYarnWidths(0, 0.6)
weave.SetXYarnHeights(0, 0.1)
weave.SetXYarnSpacings(0, 0.8)
weave.SetXYarnWidths(1, 0.6)
weave.SetXYarnHeights(1, 0.1)
weave.SetXYarnSpacings(1, 1)
weave.SetYYarnWidths(0, 0.6)
weave.SetYYarnHeights(0, 0.1)
weave.SetYYarnSpacings(0, 0.8)
weave.SetYYarnWidths(1, 0.6)
weave.SetYYarnHeights(1, 0.1)
weave.SetYYarnSpacings(1, 1)

domain = CDomainPlanes()
domain.AddPlane(PLANE(XYZ(1, 0, 0), -0.4))
domain.AddPlane(PLANE(XYZ(-1, 0, 0), -1.2))
domain.AddPlane(PLANE(XYZ(0, 1, 0), -0.3))
domain.AddPlane(PLANE(XYZ(0, -1, 0), -0.3))
domain.AddPlane(PLANE(XYZ(0, 0, 1), -0.01))
domain.AddPlane(PLANE(XYZ(0, 0, -1), -0.21))

weave.AssignDomain(domain)
textilename = AddTextile(weave)

tension = CLinearTransformation()
tension.AddScale(1.0,1.0,1.0)
deformer = CSimulationAbaqus()
deformer.SetIncludePlates( bool(0))
deformer.AddDeformationStep(tension)
deformer.SetWholeSurfaces(False)
textile = GetTextile('2DWeave(W:2,H:2)')
deformer.CreateAbaqusInputFile(textile, r'C:\Users\AQ84510\Nutstore\2\04_coding\Python\00_Projects\05_polyKriging\polykriging\test\abaqus_inp.\dryFabric.inp', bool(0),0, bool(0),1e-07)

