<core:IndoorFeatures
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    [ ... more metadata ... ]
    <gml:boundedBy> [ ... model coordinates ... ] </gml:boundedBy>

    <core:PrimalSpaceFeatures gml:id="b3ec6a1a-47c2-38f1-9b97-81ae05214735">

        <core:cellSpaceMember>
            <core:CellSpace gml:id="C1">
                <gml:description>storey="F1":type="stairs":</gml:description>
                <gml:name>stairs_storey1</gml:name>
                <core:cellSpaceGeometry>
                    <gml:surfaceMember> [ ... 5 coordinates ... ] </gml:surfaceMember>
                </core:cellSpaceGeometry>
            </core:CellSpace>
        </core:cellSpaceMember>
        [ ... more cellspaces ... ]

        <core:cellSpaceBoundaryMember>
            <core:CellSpaceBoundary gml:id="B1">
                <gml:description>type="door":</gml:description>
                <gml:name>door2</gml:name>
                <core:duality xlink:href="#T7-REVERSE"/>
                <core:cellSpaceBoundaryGeometry>
                    <gml:Polygon gml:id="CBG-B1"> [ ... 5 coordinates ... ] </gml:Polygon>
                </core:cellSpaceBoundaryGeometry>
            </core:CellSpaceBoundary>
        </core:cellSpaceBoundaryMember>
        [ ... more cellspaceboundaries ... ]

    </core:PrimalSpaceFeatures>

    <core:MultiLayeredGraph gml:id="l5419980-3f74-81b0-71df-33f5953540d7">

        <core:spaceLayers gml:id="xf8ee59b-6747-69c3-c69d-fee414bdcb10">
            <core:spaceLayerMember>
                <core:SpaceLayer gml:id="base">
                    <core:nodes gml:id="of727e25-b1ca-2f4d-dead-97319ebc2362">
                        <core:stateMember>
                            <core:State gml:id="S1">
                                <gml:description/>
                                <gml:name>S1</gml:name>
                                <core:duality xlink:href="#C1"/>
                                <core:connects xlink:href="#T1"/>
                                <core:connects xlink:href="#T4"/>
                                <core:geometry> [ ... 1 coordinate ... ] </core:geometry>
                            </core:State>
                        </core:stateMember>
                        [ ... more states ... ]
                    </core:nodes>
                    <core:edges gml:id="dff1e423-dbca-f6c2-6ea1-dbece6ee6cfe">
                        <core:transitionMember>
                            <core:Transition gml:id="T1">
                                <gml:description>type="connectivity":</gml:description>
                                <gml:name>stairs</gml:name>
                                <core:connects xlink:href="#S1"/>
                                <core:connects xlink:href="#S4"/>
                                <core:geometry> [ ... 2 coordinates ... ]  </core:geometry>
                            </core:Transition>
                        </core:transitionMember>
                        [ ... more transitions ... ]
                    </core:edges>
                </core:SpaceLayer>
            </core:spaceLayerMember>

            <core:spaceLayerMember>
                <core:SpaceLayer gml:id="F1-devices">
                    <core:nodes gml:id="a3a4c069-0566-ea69-b4b7-c816babb60ef">
                        <core:stateMember>
                            <core:State gml:id="S8">
                                <gml:description>type="smart_bulb":</gml:description>
                                <gml:name>L1</gml:name>
                                <core:geometry> [ ... 1 coordinate ... ] </core:geometry>
                            </core:State>
                        </core:stateMember>
                        [ ... more states ... ]
                    </core:nodes>
                </core:SpaceLayer>
            </core:spaceLayerMember>
            <core:spaceLayerMember>
                <core:SpaceLayer gml:id="F2-devices"> [...]
            </core:spaceLayerMember>
        </core:spaceLayers>

    </core:MultiLayeredGraph>

</core:IndoorFeatures>
