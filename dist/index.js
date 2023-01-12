/**
   Licence:
   Copyright (c) 2012-2023 Luzzi Valerio

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

   Name: spatial_ref_sys_all.js
   Purpose: This file convert spatial_ref_sys_all table into dictionary
            The table is taken by saving an ESRI Shapefile into SpatiaLite
            format 

   Author:  Luzzi Valerio

   Created: 12/01/2023
 */
import { __spatial_ref_sys_all__ } from "./spatial_ref_sys_all";

export function SpatialRefSysAll(authid) {
   authid = "" + authid;
   let srid = authid.includes(":") ? authid.split(":")[1] : authid;
   return __spatial_ref_sys_all__[srid];
}