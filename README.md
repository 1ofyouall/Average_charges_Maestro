# Average_charges_Maestro
Obtaining average atomic charges from .mol2 files in Maestro Schrodinger.

I needed to obtain ESP-charges on the atoms of a large molecule, but this structure is very difficult to optimize using quantum chemical methods. Therefore, a conformational search was conducted and for each obtained conformer, ESP-charges were calculated, which must be averaged and assigned to the final molecule. In that case we using .mol2 files exported for each conformer from Maestro Schrodinger program.

It is necessary to specify the resulting weight coefficients for each conformation file, as well as indicate the correct line numbers containing the geometry and charges of the structure.
