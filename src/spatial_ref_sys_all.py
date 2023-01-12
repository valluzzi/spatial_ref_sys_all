import sqlite3
import json
import datetime

def license():

    now = datetime.datetime.now()
    year  = datetime.date.strftime(now,"%Y")
    today = datetime.date.strftime(now,"%d/%m/%Y")
    filename = __file__.replace(".py","")

    return f"""/**
   Licence:
   Copyright (c) 2012-{year} Luzzi Valerio

   The above copyright notice and this permission notice shall be
   included in all copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
   HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
   OTHER DEALINGS IN THE SOFTWARE.

   Name: {filename}.js
   Purpose: This file convert spatial_ref_sys_all table into dictionary
            The table is taken by saving an ESRI Shapefile into SpatiaLite
            format 

   Author:  Luzzi Valerio

   Created: {today}
 */
"""

def fun():
    return """

export function SpatialRefSysAll(authid){
    authid = ""+authid
    let srid = (authid.includes(":"))?authid.split(":")[1]:authid
    return __spatial_ref_sys_all__[srid]
}
"""

def row2dict(row):
    """
    row2text
    """
    return {
       "srid": row[0],
       "auth_name": row[1],
       "ref_sys_name": row[2],
       "auth_srid": row[3],
       "is_geographic": row[4],
       "has_flipped_axes": row[5],
       "spheroid": row[6],
       "prime_meridian": row[7],
       "projection": row[8],
       "datum": row[9],
       "unit": row[10],
       "axis_1_name": row[11],
       "axis_1_orientation": row[12],
       "axis_2_name": row[13],
       "axis_2_orientation": row[14],
       "proj4text": row[15],
       "srtext":row[16],
    }



if __name__ == "__main__":
    filedb = "spatial_ref_sys_all.sqlite"
    filetxt = f"""{filedb.replace(".sqlite",".js")}"""

    conn = sqlite3.connect(filedb)

    query = """SELECT        
        [srid], 
        [auth_name], 
        [ref_sys_name], 
        [auth_srid], 
        [is_geographic], 
        [has_flipped_axes], 
        [spheroid], 
        [prime_meridian], 
        [projection], 
        [datum], 
        [unit], 
        [axis_1_name], 
        [axis_1_orientation], 
        [axis_2_name], 
        [axis_2_orientation], 
        [proj4text], 
        [srtext] FROM [spatial_ref_sys_all]"""
    cur = conn.execute(query)

    spatial_refs = {}
    for row in cur:
        srs = row2dict(row)
        spatial_refs[srs["srid"]] = srs   
    
    spatial_refs = json.dumps(spatial_refs, indent=4)
    text = license() + "const __spatial_ref_sys_all__ = " + spatial_refs + fun()
    with open(filetxt, "w") as stream:
        stream.write(text)

    